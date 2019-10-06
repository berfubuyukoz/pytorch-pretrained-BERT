from transformers import glue_processors as processors
evaluate = True
data_dir = '/home/mkbb/Desktop/fast_reach/data/sentiment_data/used/excels'
#data_dir = '/home/mkbb/Desktop/fast_reach/data/protestnews_data/edited_jsons'
processor = processors['sentiment']()
examples = processor.get_dev_examples(data_dir) if evaluate else processor.get_train_examples(data_dir)
print('lol')