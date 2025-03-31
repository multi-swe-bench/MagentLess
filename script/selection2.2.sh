date "+%Y-%m-%d %H:%M:%S"
for num in `seq 0 $(($NUM_REPRODUCTION - 1))`; do
    echo "Processing ${num}"
    python agentless/test/run_reproduction_tests.py \
        --run_id reproduction_test_generation_filter_sample_${num} \
        --test_jsonl results/$FOLDER_NAME/reproduction_test_samples/output_${num}_processed_reproduction_test.jsonl \
        --testing \
        ${TARGET_ID:+--instance_ids $TARGET_ID} \
        --dataset princeton-nlp/SWE-bench_Verified \
        --num_workers $NJ
done

