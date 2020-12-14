import tensorflow as tf

tf.enable_eager_execution()

for example in tf.data.TFRecordDataset("/home/amit/retail/workspace/training_demo/annotations/train.record"):
	
    print('-----------------------------------')
    print(tf.train.Example.FromString(example))
