import argparse
import ast
import json
import os
import subprocess
import uuid
from typing import List, Generator, Union

import pandas as pd
from tqdm import tqdm
from tree_sitter import Language, Parser, Node
import tree_sitter_cpp as tscpp
import tree_sitter_go as tsgo
import tree_sitter_java as tsjava
import tree_sitter_typescript as tsts
import tree_sitter_rust as tsrust

repo_to_top_folder = {
    # Python
    "django/django": "django",
    "sphinx-doc/sphinx": "sphinx",
    "scikit-learn/scikit-learn": "scikit-learn",
    "sympy/sympy": "sympy",
    "pytest-dev/pytest": "pytest",
    "matplotlib/matplotlib": "matplotlib",
    "astropy/astropy": "astropy",
    "pydata/xarray": "xarray",
    "mwaskom/seaborn": "seaborn",
    "psf/requests": "requests",
    "pylint-dev/pylint": "pylint",
    "pallets/flask": "flask",
    # Java
    "skylot/jadx": "jadx",
    "apache/dubbo": "dubbo",
    "apache/commons-lang": "commons-lang",
    "reactivex/rxjava": "rxjava",
    "googlecontainertools/jib": "jib",
    "netflix/eureka": "eureka",
    "apache/camel": "camel",
    "mockito/mockito": "mockito",
    "google/gson": "gson",
    "fasterxml/jackson-core": "jackson-core",
    "fasterxml/jackson-databind": "jackson-databind",
    "fasterxml/jackson-dataformat-xml": "jackson-dataformat-xml",
    "elastic/logstash": "logstash",
    "alibaba/fastjson2": "fastjson2",
    # Go
    "etcd-io/etcd": "etcd",
    "gin-gonic/gin": "gin",
    "zeromicro/go-zero": "go-zero",
    "grpc/grpc-go": "grpc-go",
    "cli/cli": "cli",
    "go-gorm/gorm": "gorm",
    # Rust
    "nushell/nushell": "nushell",
    "serde-rs/serde": "serde",
    "sharkdp/bat": "bat",
    "sharkdp/fd": "fd",
    "tokio-rs/tokio": "tokio",
    "rayon-rs/rayon": "rayon",
    "tokio-rs/bytes": "bytes",
    "tokio-rs/tracing": "tracing",
    "BurntSushi/ripgrep": "ripgrep",
    "clap-rs/clap": "clap",
    # Typescript
    "darkreader/darkreader": "darkreader",
    "vuejs/vue": "vue",
    "vuejs/core": "core",
    "mui/material-ui": "material-ui",
    # Javascript
    "anuraghazra/github-readme-stats": "github-readme-stats",
    "Kong/insomnia": "insomnia",
    "axios/axios": "axios",
    "sveltejs/svelte": "svelte",
    "expressjs/express": "express",
    "preactjs/preact": "preact",
    "iamkun/dayjs": "dayjs",
    # Cpp
    "fmtlib/fmt": "fmt",
    "nlohmann/json": "json",
    "catchorg/Catch2": "Catch2",
    "simdjson/simdjson": "simdjson",
    "yhirose/cpp-httplib": "cpp-httplib",
    # C
    "jqlang/jq": "jq",
    "redis/redis": "redis",
    "facebook/zstd": "zstd",
    "valkey-io/valkey": "valkey",
    "ponylang/ponyc": "ponyc",
}


def checkout_commit(repo_path, commit_id):
    """Checkout the specified commit in the given local git repository.
    :param repo_path: Path to the local git repository
    :param commit_id: Commit ID to checkout
    :return: None
    """
    try:
        # Change directory to the provided repository path and checkout the specified commit
        print(f"Checking out commit {commit_id} in repository at {repo_path}...")
        subprocess.run(["git", "-C", repo_path, "checkout", commit_id], check=True)
        print("Commit checked out successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running git command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def clone_repo(repo_name, repo_playground):
    try:

        print(
            f"Cloning repository from https://github.com/{repo_name}.git to {repo_playground}/{repo_to_top_folder[repo_name]}..."
        )
        dir_name = repo_to_top_folder[repo_name]
        subprocess.run(
            [
                'cp',
                f'repo/{dir_name}',
                f'{repo_playground}/{dir_name}',
                '-r',
            ],
            check=True,
        )
        print("Repository cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running git command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_project_structure_from_scratch(
    repo_name, commit_id, instance_id, repo_playground
):

    # Generate a temperary folder and add uuid to avoid collision
    repo_playground = os.path.join(repo_playground, str(uuid.uuid4()))

    # assert playground doesn't exist
    assert not os.path.exists(repo_playground), f"{repo_playground} already exists"

    # create playground
    os.makedirs(repo_playground)

    clone_repo(repo_name, repo_playground)
    checkout_commit(f"{repo_playground}/{repo_to_top_folder[repo_name]}", commit_id)
    structure = create_structure(f"{repo_playground}/{repo_to_top_folder[repo_name]}")
    # clean up
    subprocess.run(
        ["rm", "-rf", f"{repo_playground}/{repo_to_top_folder[repo_name]}"], check=True
    )
    d = {
        "repo": repo_name,
        "base_commit": commit_id,
        "structure": structure,
        "instance_id": instance_id,
    }
    return d


def parse_python_file(file_path, file_content=None):
    """Parse a Python file to extract class and function definitions with their line numbers.
    :param file_path: Path to the Python file.
    :return: Class names, function names, and file contents
    """
    if file_content is None:
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                parsed_data = ast.parse(file_content)
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""
    else:
        try:
            parsed_data = ast.parse(file_content)
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""

    class_info = []
    function_names = []
    class_methods = set()

    for node in ast.walk(parsed_data):
        if isinstance(node, ast.ClassDef):
            methods = []
            for n in node.body:
                if isinstance(n, ast.FunctionDef):
                    methods.append(
                        {
                            "name": n.name,
                            "start_line": n.lineno,
                            "end_line": n.end_lineno,
                            "text": file_content.splitlines()[
                                n.lineno - 1 : n.end_lineno
                            ],
                        }
                    )
                    class_methods.add(n.name)
            class_info.append(
                {
                    "name": node.name,
                    "start_line": node.lineno,
                    "end_line": node.end_lineno,
                    "text": file_content.splitlines()[
                        node.lineno - 1 : node.end_lineno
                    ],
                    "methods": methods,
                }
            )
        elif isinstance(node, ast.FunctionDef) and not isinstance(
            node, ast.AsyncFunctionDef
        ):
            if node.name not in class_methods:
                function_names.append(
                    {
                        "name": node.name,
                        "start_line": node.lineno,
                        "end_line": node.end_lineno,
                        "text": file_content.splitlines()[
                            node.lineno - 1 : node.end_lineno
                        ],
                    }
                )

    return class_info, function_names, file_content.splitlines()


def traverse(node: Node) -> Generator[Node, None, None]:
    cursor = node.walk()
    visited_children = False
    while True:
        if not visited_children:
            yield cursor.node
            if not cursor.goto_first_child():
                visited_children = True
        elif cursor.goto_next_sibling():
            visited_children = False
        elif not cursor.goto_parent():
            break


def get_child(node: Node, type_name: str, skip: int = 0) -> Union[Node, None]:
    for child in node.children:
        if child.type == type_name:
            if skip == 0:
                return child
            skip = skip - 1
    return None


def get_child_chain(node: Node, type_names: List[str]) -> Union[str, None]:
    for type_name in type_names:
        node = get_child(node, type_name)
        if node is None:
            return node
    return node


def get_name(node: Node, type_name: str = 'identifier') -> Union[str, None]:
    return get_child(node, type_name).text.decode('utf-8')


def parse_java_file(file_path, file_content=None):
    """Parse a Java file to extract interface definitions and class definitions with their line numbers.
    :param file_path: Path to the Java file.
    :return: Class names, and file contents
    """
    parser = Parser(Language(tsjava.language()))

    if file_content is None:
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], ""
    else:
        try:
            tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], ""

    class_info = []

    for node in traverse(tree.root_node):
        if node.type == "interface_declaration" or node.type == "class_declaration":
            info = None
            if node.type == "interface_declaration":
                info = class_info
            elif node.type == "class_declaration":
                info = class_info

            methods = []
            for n in traverse(node):
                if n.type == "method_declaration":
                    methods.append(
                        {
                            "name": get_name(n),
                            "start_line": n.start_point.row,
                            "end_line": n.end_point.row,
                            "text": n.text.decode('utf-8').splitlines(),
                        }
                    )
            info.append(
                {
                    "name": get_name(node),
                    "start_line": node.start_point.row,
                    "end_line": node.end_point.row,
                    "text": node.text.decode('utf-8').splitlines(),
                    "methods": methods,
                }
            )

    return class_info, file_content.splitlines()


def parse_go_file(file_path, file_content=None):
    """Parse a Go file to extract class and function definitions with their line numbers.
    :param file_path: Path to the Python file.
    :return: Class names, function names, and file contents
    """
    parser = Parser(Language(tsgo.language()))

    if file_content is None:
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""
    else:
        try:
            tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""

    class_info = []
    function_names = []

    for node in traverse(tree.root_node):
        if node.type == "type_declaration":
            type_spec = get_child(node, 'type_spec')
            if type_spec is None:
                continue
            name = get_name(type_spec, 'type_identifier')
            methods = []
            class_info.append({
                'name': name,
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
                'methods': methods,
            })
        elif node.type == 'method_declaration':
            function_names.append({
                'name': get_name(node, 'field_identifier'),
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
            })
        elif node.type == 'function_declaration':
            function_names.append({
                'name': get_name(node, 'identifier'),
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
            })

    return class_info, function_names, file_content.splitlines()


def parse_rust_file(file_path, file_content=None):
    """Parse a Rust file to extract class and function definitions with their line numbers.
    :param file_path: Path to the Python file.
    :return: Class names, function names, and file contents
    """
    parser = Parser(Language(tsrust.language()))

    if file_content is None:
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""
    else:
        try:
            tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""

    class_info = []
    function_names = []
    class_to_methods = {}

    def get_type(node: Node):
        if node.type == 'type_identifier':
            return node.text.decode('utf-8')
        elif node.type == 'generic_type':
            return get_type(node.child_by_field_name('type'))
        return None

    for node in traverse(tree.root_node):
        if node.type == 'struct_item' or node.type == 'enum_item':
            name = get_name(node, 'type_identifier')
            methods = []
            class_to_methods[name] = methods
            class_info.append({
                'name': name,
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
                'methods': methods,
            })
        elif node.type == 'impl_item':
            class_ = get_type(node.child_by_field_name('type'))
            methods = class_to_methods.get(class_, None)
            if methods is not None:
                for child in traverse(node):
                    if child.type == 'function_item':
                        methods.append({
                            'name': get_name(child),
                            'start_line': child.start_point.row,
                            'end_line': child.end_point.row,
                            'text': child.text.decode('utf-8').splitlines(),
                        })
        elif node.type == 'function_item':
            function_names.append({
                'name': get_name(node),
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
            })

    return class_info, function_names, file_content.splitlines()


def parse_cpp_file(file_path, file_content=None):
    """Parse a Cpp file to extract class and function definitions with their line numbers.
    :param file_path: Path to the Python file.
    :return: Class names, function names, and file contents
    """
    parser = Parser(Language(tscpp.language()))

    if file_content is None:
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""
    else:
        try:
            tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""

    class_info = []
    function_names = []

    def get_type(node: Node):
        if node.type == 'type_identifier':
            return node.text.decode('utf-8')
        elif node.type == 'template_type':
            return get_type(node.child_by_field_name('name'))
        return None

    for node in traverse(tree.root_node):
        if node.type == 'class_specifier':
            methods = []
            if file_path.endswith('.c'):
                continue
            class_info.append({
                'name': get_type(node.child_by_field_name('name')),
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
                'methods': methods,
            })
            for child in traverse(node):
                if child.type == 'function_definition':
                    name_node = child.child_by_field_name('declarator')
                    name_node = name_node.child_by_field_name('declarator')
                    if name_node is None:
                        continue
                    methods.append({
                        'name': name_node.text.decode('utf-8'),
                        'start_line': child.start_point.row,
                        'end_line': child.end_point.row,
                        'text': child.text.decode('utf-8').splitlines(),
                    })
        elif node.type == 'function_definition':
            name_node = node.child_by_field_name('declarator')
            name_node = name_node.child_by_field_name('declarator')
            if name_node is None:
                continue

            in_class = False
            tmp = node
            while tmp != tree.root_node:
                if tmp.type == 'class_specifier':
                    in_class = True
                    break
                tmp = tmp.parent
            if in_class:
                continue

            function_names.append({
                'name': name_node.text.decode('utf-8'),
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
            })

    return class_info, function_names, file_content.splitlines()


def parse_typescript_file(file_path, file_content=None):
    """Parse a Typescript file to extract interface definitions and class definitions with their line numbers.
    :param file_path: Path to the Java file.
    :return: Class names, function names, and file contents
    """
    parser = Parser(Language(tsts.language_typescript()))

    if file_content is None:
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""
    else:
        try:
            tree = parser.parse(bytes(file_content, "utf-8"))
        except Exception as e:  # Catch all types of exceptions
            print(f"Error in file {file_path}: {e}")
            return [], [], ""

    class_info = []
    function_names = []
    arrow_function_idx = 0

    for node in traverse(tree.root_node):
        if node.type == 'class_declaration':
            methods = []
            class_info.append({
                'name': node.child_by_field_name('name').text.decode('utf-8'),
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
                'methods': methods,
            })
            for child in traverse(node):
                if child.type == 'method_definition':
                    methods.append({
                        'name': child.child_by_field_name('name').text.decode('utf-8'),
                        'start_line': child.start_point.row,
                        'end_line': child.end_point.row,
                        'text': child.text.decode('utf-8').splitlines(),
                    })
        elif node.type == 'function_declaration':
            function_names.append({
                'name': node.child_by_field_name('name').text.decode('utf-8'),
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
            })
        elif node.type == 'arrow_function':
            function_names.append({
                'name': f'arrow_function_{arrow_function_idx}',
                'start_line': node.start_point.row,
                'end_line': node.end_point.row,
                'text': node.text.decode('utf-8').splitlines(),
            })
            arrow_function_idx = arrow_function_idx + 1

    return class_info, function_names, file_content.splitlines()


def check_file_ext(file_name, language):
    exts = {
        'cpp': ['h', 'hpp', 'hxx', 'c', 'cpp', 'cc', 'cxx'],
        'typescript': ['js', 'ts'],
    }
    file_name = file_name.lower()
    for ext in exts[language]:
        if file_name.endswith(f'.{ext}'):
            return True
    return False


def create_structure(directory_path):
    """Create the structure of the repository directory by parsing Python files.
    :param directory_path: Path to the repository directory.
    :return: A dictionary representing the structure.
    """
    structure = {}

    for root, _, files in os.walk(directory_path):
        repo_name = os.path.basename(directory_path)
        relative_root = os.path.relpath(root, directory_path)
        if relative_root == ".":
            relative_root = repo_name
        curr_struct = structure
        for part in relative_root.split(os.sep):
            if part not in curr_struct:
                curr_struct[part] = {}
            curr_struct = curr_struct[part]
        for file_name in files:
            if file_name.endswith(".py"):
                file_path = os.path.join(root, file_name)
                class_info, function_names, file_lines = parse_python_file(file_path)
                curr_struct[file_name] = {
                    "classes": class_info,
                    "functions": function_names,
                    "text": file_lines,
                }
            elif file_name.endswith('.java'):
                file_path = os.path.join(root, file_name)
                class_info, file_lines = parse_java_file(file_path)
                curr_struct[file_name] = {
                    'classes': class_info,
                    'functions': [],
                    'text': file_lines,
                }
            elif file_name.endswith('.go'):
                file_path = os.path.join(root, file_name)
                class_info, function_names, file_lines = parse_go_file(file_path)
                curr_struct[file_name] = {
                    "classes": class_info,
                    "functions": function_names,
                    "text": file_lines,
                }
            elif file_name.endswith('.rs'):
                file_path = os.path.join(root, file_name)
                class_info, function_names, file_lines = parse_rust_file(file_path)
                curr_struct[file_name] = {
                    "classes": class_info,
                    "functions": function_names,
                    "text": file_lines,
                }
            elif check_file_ext(file_name, 'cpp'):
                file_path = os.path.join(root, file_name)
                class_info, function_names, file_lines = parse_cpp_file(file_path)
                curr_struct[file_name] = {
                    "classes": class_info,
                    "functions": function_names,
                    "text": file_lines,
                }
            elif check_file_ext(file_name, 'typescript'):
                file_path = os.path.join(root, file_name)
                class_info, function_names, file_lines = parse_typescript_file(file_path)
                curr_struct[file_name] = {
                    "classes": class_info,
                    "functions": function_names,
                    "text": file_lines,
                }
            else:
                curr_struct[file_name] = {}

    return structure

