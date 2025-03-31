date "+%Y-%m-%d %H:%M:%S"
python agentless/fl/localize.py \
    --fine_grain_line_level \
    --output_folder results/$FOLDER_NAME/edit_location_samples \
    --top_n 3 \
    --compress \
    --temperature 0.8 \
    --num_samples $NUM_SETS \
    --start_file results/$FOLDER_NAME/related_elements/loc_outputs.jsonl \
    --num_threads $NJ \
    --dataset $DATASET \
    --split $SPLIT \
    ${TARGET_ID:+--target_id $TARGET_ID} \
    --skip_existing

