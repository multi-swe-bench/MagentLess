date "+%Y-%m-%d %H:%M:%S"
python agentless/fl/localize.py \
    --related_level \
    --output_folder results/$FOLDER_NAME/related_elements \
    --top_n 3 \
    --compress_assign \
    --compress \
    --start_file results/$FOLDER_NAME/file_level_combined/combined_locs.jsonl \
    --num_threads $NJ \
    --dataset $DATASET \
    --split $SPLIT \
    ${TARGET_ID:+--target_id $TARGET_ID} \
    --skip_existing

