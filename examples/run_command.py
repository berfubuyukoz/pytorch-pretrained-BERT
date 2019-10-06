import os
command = 'python ./run_glue.py ' \
          '--data_dir /home/mkbb/Desktop/fast_reach/data/protestnews_data/edited_jsons_transfomers ' \
          '--model_type distilbert ' \
          '--model_name_or_path distilbert-base-uncased ' \
          '--task_name protestnews ' \
          '--output_dir /home/mkbb/Desktop/fast_reach/models_outs/finetuned_models_outs/with_transformers/bert_finetune_india ' \
          '--per_gpu_train_batch_size 32 --per_gpu_eval_batch_size 32'
os.system(command)