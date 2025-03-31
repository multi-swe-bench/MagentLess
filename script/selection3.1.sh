date "+%Y-%m-%d %H:%M:%S"
folders=`ls results/$FOLDER_NAME/repair_sample_* -d | paste -sd ','`
python agentless/repair/rerank.py \
    --patch_folder $folders \
    --num_samples $(($NUM_SETS * $NUM_SAMPLES_PER_SET)) \
    --deduplicate \
    --output_file results/$FOLDER_NAME/all_preds.jsonl

