date "+%Y-%m-%d %H:%M:%S"
python -m swebench.harness.run_evaluation \
    --dataset_name princeton-nlp/SWE-bench_Verified \
    --predictions results/$FOLDER_NAME/all_preds.jsonl \
    --max_workers $NJ \
    --run_id evaluation_${FOLDER_NAME}
