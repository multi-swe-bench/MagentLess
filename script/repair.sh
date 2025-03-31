date "+%Y-%m-%d %H:%M:%S"
for i in `seq 1 ${NUM_SETS}`; do
    ii=$(($i - 1))
    python agentless/repair/repair.py \
        --loc_file results/$FOLDER_NAME/edit_location_individual/loc_merged_${ii}-${ii}_outputs.jsonl \
        --output_folder results/$FOLDER_NAME/repair_sample_${i} \
        --loc_interval \
        --top_n 3 \
        --context_window 10 \
        --max_samples ${NUM_SAMPLES_PER_SET} \
        --cot \
        --diff_format \
        --gen_and_process \
        --dataset $DATASET \
        --split $SPLIT \
        ${TARGET_ID:+--target_id $TARGET_ID} \
        --num_threads $NJ
done

