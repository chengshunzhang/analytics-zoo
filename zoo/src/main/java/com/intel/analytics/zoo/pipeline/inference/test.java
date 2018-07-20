package com.intel.analytics.zoo.pipeline.inference;
import java.util.Random;
import java.util.List;
import java.util.ArrayList;
public class test {
    public static class InferenceModel extends AbstractInferenceModel{}
    public static void main(String[] args){
       InferenceModel t = new InferenceModel();
       t.loadTF("/home/chengshunzhang/tfnet/inception_v1");
       float[] Arr = new float[224*224*3];
       Random random = new Random();
       for (int i = 0; i < 224*224*3; i++){
           Arr[i] = random.nextFloat();
       }
       int[] Shape = {224,224,3};
       List<JTensor> JT = new ArrayList<JTensor>();
       JT.add(new JTensor(Arr,Shape));
       t.predict(JT);
    }
}
