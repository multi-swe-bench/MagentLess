date "+%Y-%m-%d %H:%M:%S"
python agentless/test/run_regression_tests.py \
    --run_id generate_regression_tests \
    --output_file results/$FOLDER_NAME/passing_tests.jsonl \
    ${TARGET_ID:+--instance_ids $TARGET_ID} \
    --dataset $DATASET \
    --split $SPLIT 
