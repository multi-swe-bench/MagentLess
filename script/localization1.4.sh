date "+%Y-%m-%d %H:%M:%S"
python agentless/fl/combine.py \
    --retrieval_loc_file results/$FOLDER_NAME/retrievel_embedding/retrieve_locs.jsonl \
    --model_loc_file results/$FOLDER_NAME/file_level/loc_outputs.jsonl \
    --top_n 3 \
    --output_folder results/$FOLDER_NAME/file_level_combined

