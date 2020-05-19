# RecurrentLIF

Here we want to simulate the biological network with LIF neurons as a recurrent of recurrent neural network.


### For the LIF analysis
The LIF neuron is biologically plausible with complex physical dynamics on timing. Rather than implementing circuits that deliberately route signals back to the input, the recurrence relationship occurs naturally in the time dynamics of the physical LIF neuron itself. The non-differential membrane potential reset after reaching threshold is also an alternative gate controling, which makes the information in biological system sparser compared with the counterpart ANNs. The integration of LIF neuron and recurrent loop structure may the key to analyzing the power of processing sequential information in the biological brain. 

The mathematical description of biological LIF neuron is given as below, which shows the characteristics of the neural activity (e.g. membrane potential V) accumulation from its history.

$$ \tau \frac{dV}{dt} =g_l(V_l-V) + I$$

After the finite difference discretization, the equation can be written as:

$$ V_t - V_{t-1} = (g_lV_l-g_lV_{t-1}+I)\tau\Delta t$$
$$ V_t = (1-\frac{g_l}{\tau})V_{t-1}+ \frac{g_l}{\tau}V_l + \frac{I}{\tau}$$



second-order partial differential equation

### For the RNN analysis

The recurrent loop in ANNs is usually called recurrent neural network (RNN) which is carefully designed as the basic  preconditional structure for sequential information processing. The mathematically description of RNN is is shown as:

$$ h_t=\sigma^h (w^h h_{t-1} + w^x x_t) $$ 
$$ y_t = \sigma^y(w^y h_t) $$ 

$x$, $h_t$, $h_{t-1}$, $y$, $\sigma^h()$ and $\sigma^y()$ are non-linear activation functions for hidden and output states. 
Trainable dense matrices $w^h$, $w^x$ and $w^y$.

### The recurrent network with LIF neurons

Then The recurrent loop in LIF neuron can be considered as another integrator which shows the second-order integration of the original neural activity V(t), represented as $A(t)$, in which $A(t) = detV = V(t)-V(t-1)$. This architecture should result in the reduction of energy consumption and gain of complex sequential information representation. 


### Equivalence between LIF neuron and RNN

In the operation of both LIF neuron or an RNN, the neuron states will be updated by step-by-step processing. The neuronal state in pre-steps will be accumulated as the historial momory in the hidden state of neuron as $h$. The hidden state makes neuron save the memory of previous steps with different degree of emphasis, for example, the standard RNN has exponential decay of $V_{t-k}$ with past time $k$, another example is LSTM, which has learned scalars for $V_{t-k}$ ($k$ is passed frames) for long-term or short-term memories. 

learn temporal features with long or short dependencies, 


### Training an recurrent LIF during sequantial learning




### Figures

Figure 1, the conceptual comparisons of A and B

