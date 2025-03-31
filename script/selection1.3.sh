date "+%Y-%m-%d %H:%M:%S"
for i in `seq 1 ${NUM_SETS}`; do
    folder=results/$FOLDER_NAME/repair_sample_${i}
    for num in `seq 0 $(($NUM_SAMPLES_PER_SET - 1))`; do
        run_id_prefix=`basename $folder`
        python agentless/test/run_regression_tests.py \
            --regression_tests results/$FOLDER_NAME/select_regression/output.jsonl \
            --predictions_path $folder/output_${num}_processed.jsonl \
            --run_id ${run_id_prefix}_regression_${num} \
            ${TARGET_ID:+--instance_ids $TARGET_ID} \
            --dataset princeton-nlp/SWE-bench_Verified \
            --num_workers $NJ
    done
done

