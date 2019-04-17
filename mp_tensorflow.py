# Keras
def ModelFunc(i,SomeData):
    import keras
    YourModel = Here
    return(ModelScore)

pool = Pool(processes = 4)
for i,Score in enumerate(pool.imap(partial(ModelFunc,SomeData),range(4))):
    print(Score)


# Tensorflow
import tensorflow as tf

class Model:
    def __init__(self,param):
        self.param = param

        # create & build graph
        self.graph = tf.Graph()
        self.build_graph()

        # create session
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        gpu_num = random.choice(cuda_gpu_count())
        config.gpu_options.visible_device_list= str(gpu_num)
        self.sess = tf.Session(config=config,graph=self.graph)

    def build_graph(self):
        with self.graph.as_default():
            ...
    def __del__(self):
        # explicitly collect resources by closing and deleting session and graph
        self.sess.close()
        del self.sess
        del self.graph
        del self.param

    # train models and return the test accuracy
    def train_test(self,train_data,train_label,test_data,test_label):
        ...


with Pool(process_num) as p:
    accuracies = p.map(lambda param:Model(param).train_test(train_data,train_label,test_data,test_label), hyper_parameter_list)

# 有 bug
# 解决方案是：将gpu_num与process_id绑定（理由见 踩坑实录），即相同的process_id运行该程序时，均使用相同的GPU。更改的样例代码如下：

class Model:    
    def __init__(self,param):
        gpu_num = os.getpid()%cuda_gpu_count()
        config.gpu_options.visible_device_list= str(gpu_num)
        self.sess = tf.Session(config=config,graph=self.graph)

with Pool(process_num) as p:
    accuracies = p.map(lambda param:Model(param).train_test(train_data,train_label,test_data,test_label), hyper_parameter_list)

