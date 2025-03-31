set -x

# api_key.sh
# export OPENAI_API_KEY=
# export OPENAI_BASE_URL=
# export OPENAI_MODEL=
# export OPENAI_EMBED_URL=
source script/api_key.sh

export PYTHONPATH=`pwd`
export TARGET_ID=
export NJ=50
export NUM_SETS=2
export NUM_SAMPLES_PER_SET=2
export NUM_REPRODUCTION=4
export FOLDER_NAME=typescript_verified_4o
export SWEBENCH_LANG=typescript
export PROJECT_FILE_LOC=structure
export DATASET=local_json
export SPLIT=java_verified

./script/localization1.1.sh
./script/localization1.2.sh
./script/localization1.3.sh
./script/localization1.4.sh
./script/localization2.1.sh
./script/localization3.1.sh
./script/localization3.2.sh

./script/repair.sh

#./script/selection1.1.sh
#./script/selection1.2.sh
#./script/selection1.3.sh
#./script/selection2.1.sh
#./script/selection2.2.sh
#./script/selection2.3.sh
#./script/selection2.4.sh
./script/selection3.1.sh

./script/evaluation.sh
