date "+%Y-%m-%d %H:%M:%S"
python agentless/test/generate_reproduction_tests.py \
    --max_samples $NUM_REPRODUCTION \
    --output_folder results/$FOLDER_NAME/reproduction_test_samples \
    --output_file reproduction_tests.jsonl \
    --num_threads $NJ \
    ${TARGET_ID:+--target_id $TARGET_ID} \
    --select \
    --dataset princeton-nlp/SWE-bench_Verified
