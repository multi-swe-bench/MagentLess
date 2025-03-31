date "+%Y-%m-%d %H:%M:%S"
for i in `seq 1 $NUM_SETS`; do
    folder=results/$FOLDER_NAME/repair_sample_${i}
    for num in `seq 0 $(($NUM_SAMPLES_PER_SET - 1))`; do
        run_id_prefix=$(basename $folder)
        python agentless/test/run_reproduction_tests.py \
            --test_jsonl results/$FOLDER_NAME/reproduction_test_samples/reproduction_tests.jsonl \
            --predictions_path $folder/output_${num}_processed.jsonl \
            --run_id ${run_id_prefix}_reproduction_${num} \
            ${TARGET_ID:+--instance_ids $TARGET_ID} \
            --dataset princeton-nlp/SWE-bench_Verified \
            --num_workers $NJ
    done
done

