date "+%Y-%m-%d %H:%M:%S"
python agentless/fl/localize.py \
    --file_level \
    --irrelevant \
    --output_folder results/$FOLDER_NAME/file_level_irrelevant \
    --num_threads $NJ \
    --dataset $DATASET \
    --split $SPLIT \
    ${TARGET_ID:+--target_id $TARGET_ID} \
    --skip_existing

