from StimulusGenerator import *

if __name__ == "__main__":
    stimulus_generator = StimulusGenerator(
        scaling=2,
        range=0.5,
        omega=5.7,
        diameter=0.7,
        side_length=7,
        grating_res=50,
        contrast_res=480
    )
    stimulus = stimulus_generator.generate()
    print("stimulus: \n", stimulus.shape)



