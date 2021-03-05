# Image Captioning

The goal of image captioning is to convert a given input image into a natural language description. The encoder-decoder framework is widely used for this task. The image encoder is a convolutional neural network (CNN), the resnet-152 model pretrained on the ILSVRC-2012-CLS image classification dataset. The decoder is a long short-term memory (LSTM) network.

#### Encoder-Decoder Architecture
Typically, a model that generates sequences will use an Encoder to encode the input into a fixed form and a Decoder to decode it, word by word, into a sequence.

#### Attention Mechanism
This is a way for a model to choose only those parts of the encoding that it thinks is relevant to the task at hand. In image captioning, you consider some pixels more important than others. In sequence to sequence tasks like machine translation, you consider some words more important than others.

#### Encoder

The Encoder encodes the input image with 3 color channels into a smaller image with "learned" channels. This smaller encoded image is a summary representation of all that's useful in the original image. Since we want to encode images, we use Convolutional Neural Networks (CNNs). These models progressively create smaller and smaller representations of the original image, and each subsequent representation is more "learned", with a greater number of channels. The final encoding produced by our ResNet-151 encoder has a size of 14x14 with 2048 channels, i.e., a 2048, 14, 14 size tensor.

#### Decoder

The Decoder's job is to look at the encoded image and generate a caption word by word. Since it's generating a sequence, it would need to be a Recurrent Neural Network (RNN). We will use an LSTM. 
In a setting with Attention, we want the Decoder to be able to look at different parts of the image at different points in the sequence. For example, while generating the word football in a man holds a football, the Decoder would know to focus on – you guessed it – the football!

# semantic-text-similarity

An easy-to-use interface to fine-tuned BERT models for computing semantic similarity. 
This project contains an interface to fine-tuned, BERT-based semantic text similarity models. It modifies pytorch-transformers by abstracting away all the research benchmarking code for ease of real-world applicability.


# Setup

#### 1. Dependencies

```bash
pip install -r requirements.txt
pip3 install -r requirements.txt
pip install semantic-text-similarity
```

#### 2. Download the pretrained Weights

Download the pretrained model [here](https://www.dropbox.com/s/ne0ixz5d58ccbbz/pretrained_model.zip?dl=0) and the vocabulary file [here](https://www.dropbox.com/s/26adb7y9m98uisa/vocap.zip?dl=0). Extract pretrained_model.zip to `./models/` and vocab.pkl to `./data/` using `unzip` command.

Alternate download link: [Google Drive](https://drive.google.com/drive/folders/1_ZGIZcb4l2rctktDaFuDYu691RYZdghP?usp=sharing)

Once it is downloaded, unzip them.

```bash
unzip pretrained_model.zip -d models
unzip vocap.zip -d data
```


#### 3. Predict

```bash
python predict.py
```

OR

```bash
python3 predict.py
```
