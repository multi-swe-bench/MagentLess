date "+%Y-%m-%d %H:%M:%S"
python agentless/test/select_regression_tests.py \
    --passing_tests results/$FOLDER_NAME/passing_tests.jsonl \
    --output_folder results/$FOLDER_NAME/select_regression \
    ${TARGET_ID:+--instance_ids $TARGET_ID} \
    --dataset princeton-nlp/SWE-bench_Verified
