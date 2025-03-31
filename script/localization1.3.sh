date "+%Y-%m-%d %H:%M:%S"
python agentless/fl/retrieve.py \
    --index_type simple \
    --filter_type given_files \
    --filter_file results/$FOLDER_NAME/file_level_irrelevant/loc_outputs.jsonl \
    --output_folder results/$FOLDER_NAME/retrievel_embedding \
    --persist_dir embedding/swe-bench_simple \
    --num_threads $NJ \
    --dataset $DATASET \
    --split $SPLIT \
    ${TARGET_ID:+--target_id $TARGET_ID}

