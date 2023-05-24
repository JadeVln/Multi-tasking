
from expyriment import design, control, stimuli, io, misc
import random 

#Colors 
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)

MAX_REP_DURATION = 4000
LOSANGE_OR_TWO_DOTS_KEY = 'b'
SQUARE_OR_THREE_DOTS_KEY = 'n'

INTERTRIAL_DURATION = 800

TRAINING_TRIALS_PER_BLOCK = 4
TRIALS_PER_BLOCK = 6


exp = design.Experiment(name=" Multitasking Experiment", background_colour = GREY)
#control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment
control.defaults.auto_create_subject_id = True
control.defaults.initialize_delay = 5

control.initialize(exp)

#Load the frame and stimuli images
W, H = exp.screen.window_size 

#Create rectangle frame and labels 
frame = stimuli.Rectangle((.6*W, .8*H), colour=BLACK, line_width=10)
line = stimuli.Line((-.3*W, 0), (.3*W, 0), colour=BLACK, line_width=10)
label_top = stimuli.TextLine("SHAPE", position= (0, 0.45*H), text_size=80, text_colour=BLACK)  
label_bottom = stimuli.TextLine("FILLING", position=(0, -0.45*H), text_size=80, text_colour=BLACK) 


#Create a function to create the canvas with the frame and the stimulus 

def create_canvas(stim, position) : 
    if position == 'up' : 
        stim.reposition((0, 0.2 * H))
    else : 
        stim.reposition((0, -0.2 * H))

    stim.scale((0.7, 0.7))
    canvas = stimuli.Canvas((W, H))
    stim.plot(canvas)
    frame.plot(canvas)
    line.plot(canvas)
    label_top.plot(canvas)
    label_bottom.plot(canvas)

    return canvas
"""
def create_canvas_down(stim) : 
    stim.reposition((0, -0.2 * H))
    stim.scale((0.7, 0.7))

    canvas = stimuli.Canvas((W, H))
    stim.plot(canvas)
    frame.plot(canvas)
    line.plot(canvas)
    label_top.plot(canvas)
    label_bottom.plot(canvas)

    return canvas
"""

#Load all the stimuli images into variables 
square_2u = stimuli.Picture("square_2.png")
square_2d = stimuli.Picture("square_2.png")
square_3u = stimuli.Picture("square_3.png")
square_3d = stimuli.Picture("square_3.png")
losange_2u = stimuli.Picture("losange_2.png")
losange_2d = stimuli.Picture("losange_2.png")
losange_3u = stimuli.Picture("losange_3.png")
losange_3d = stimuli.Picture("losange_3.png")


#Use the functions to create the 8 canvas 
# Create the canvas with the stimuli at the top 
canvas_s2u = create_canvas(square_2u, 'up')
canvas_s3u = create_canvas(square_3u, 'up')
canvas_l2u = create_canvas(losange_2u, 'up')
canvas_l3u = create_canvas(losange_3u, 'up')

# Create the canvas with the stimuli at the bottom
canvas_s2d = create_canvas(square_2d, 'down')
canvas_s3d = create_canvas(square_3d, 'down')
canvas_l2d = create_canvas(losange_2d, 'down')
canvas_l3d = create_canvas(losange_3d, 'down')

up = [canvas_s2u, canvas_s3u, canvas_l2u, canvas_l3u]
down = [canvas_s2d, canvas_s3d, canvas_l2d, canvas_l3d]

square = [canvas_s2u, canvas_s2d, canvas_s3u, canvas_s3d]
losange = [canvas_l2u, canvas_l2d, canvas_l3u, canvas_l3d]

deux_dots = [canvas_s2u, canvas_s2d, canvas_l2u, canvas_l2d]
trois_dots = [canvas_s3u, canvas_s3d, canvas_l3u, canvas_l3d]

# Define a function to create the 6 blocks (3 training blocks and 3 blocks for data analysis)
def create_block(name, stimulus_c, stimulus_in, num_trials) : 
    block = design.Block(name=name)
    for _ in range(num_trials//2):
        trial = design.Trial()
        choice_stim = random.choice(stimulus_c)
        if choice_stim in up :
            trial.set_factor("Task", "Shape")
        else : 
            trial.set_factor("Task", "Filling")

        if choice_stim in square : 
            trial.set_factor("Form", "Square")
        else :  
            trial.set_factor("Form", "Losange")

        if choice_stim in deux_dots : 
                trial.set_factor("Dots", "Two")
        else : 
                trial.set_factor("Dots", "Three")

        trial.add_stimulus(choice_stim)
        block.add_trial(trial)

        trial = design.Trial()
        choice_stim = random.choice(stimulus_in)
        trial.add_stimulus(choice_stim)
        if choice_stim in up :
            trial.set_factor("Task", "Shape")
        else : 
            trial.set_factor("Task", "Filling")

        if choice_stim in square : 
            trial.set_factor("Form", "Square")
        else :  
            trial.set_factor("Form", "Losange")

        if choice_stim in deux_dots : 
            trial.set_factor("Dots", "Two")
        else : 
            trial.set_factor("Dots", "Three")
        block.add_trial(trial)
    block.shuffle_trials()


    return block 


#Create list of stimuli for the different blocks 
# incongruent stimuli : canvas_l3# and canvas_s2#
# congruent stimuli : canvas_l2# and canvas_s3#
# stimuli for shape task : canvas_##u
# stimuli for filling task : canvas_##d

stimuli_in = [canvas_l3u, canvas_s2u, canvas_l3d, canvas_s2d]
stimuli_c = [canvas_l2u, canvas_s3u, canvas_l2d, canvas_s3d]

stimuli_shape_in= [canvas_l3u, canvas_s2u]
stimuli_shape_c = [canvas_l2u, canvas_s3u]

stimuli_filling_in = [canvas_l3d, canvas_s2d]
stimuli_filling_c = [canvas_l2d, canvas_s3d]


# Create blocks and trials for training
blocks =[]

blocks.append(create_block("Shape Task Training Block", stimuli_shape_c, stimuli_shape_in, TRAINING_TRIALS_PER_BLOCK))
blocks.append(create_block("Filling Task Training Block", stimuli_filling_c, stimuli_filling_in, TRAINING_TRIALS_PER_BLOCK))
blocks.append(create_block("Mixed Task Block", stimuli_c, stimuli_in, TRAINING_TRIALS_PER_BLOCK))
blocks.append(create_block("Shape Task Block", stimuli_shape_c, stimuli_shape_in, TRIALS_PER_BLOCK))
blocks.append(create_block("Filling Task Block", stimuli_filling_c, stimuli_filling_in, TRIALS_PER_BLOCK))
blocks.append(create_block("Mixed Task Block", stimuli_c, stimuli_in, TRIALS_PER_BLOCK))


#Create list of stimuli for the feedback message

REP_B = [canvas_l2u, canvas_l3u, canvas_l2d, canvas_s2d]
REP_N = [canvas_s2u, canvas_s3u, canvas_l3d, canvas_s3d]

# Feedback message function
def show_feedback(trial, key):
    stimulus = trial.stimuli[0]
    REMINDER_KEY_STIMULUS = False
    feedback_text = ''

    if key == None : 
        feedback_text = 'Time is up'
        REMINDER_KEY_STIMULUS = True 
    else : 
        if stimulus in REP_B : 
            if key !=  LOSANGE_OR_TWO_DOTS_KEY : 
                feedback_text = "That was the wrong key"
                REMINDER_KEY_STIMULUS = True 
        elif stimulus in REP_N : 
            if key != SQUARE_OR_THREE_DOTS_KEY : 
                feedback_text = "That was the wrong key"
                REMINDER_KEY_STIMULUS = True 

    feedback = stimuli.TextLine(feedback_text, position=(0, 0), text_size=60, text_colour=BLACK)
    feedback.present()
    exp.clock.wait(1000)  # Display feedback for 1 second
    feedback.unload()

    if REMINDER_KEY_STIMULUS == True : 
        reminder.present()
        exp.clock.wait(5000)  # Display reminder for 5 seconds
        reminder.unload()
        blankscreen.present()
        exp.clock.wait(500)



control.start(skip_ready_screen=True)

exp.data.add_variable_names(['Block Name', 'Task', 'Stimulus Shape', 'Stimulus Filling', 'Response Key', 'Reaction Time'])

blankscreen = stimuli.BlankScreen()

instructions = stimuli.TextScreen('Instructions', f"""In the following experiment, you will respond to four different figures : 

-   Diamond with filling of 3 dots 
-   Diamond with filling of 2 dots 
-   Square with filling of 3 dots 
-   Square with filling of 2 dots

You will be show these figures in sequences of trials. Each time you will need to respond either 
with the B keyboard button or with the N keyboard button.

If the stimulus appear in the upper frame, it is the shape task. You need to ignore the filling (dots) of the shape. 
If the shape is a diamond, you need to press B. 
If the shape is a square, you need to press N. 

If the stimulus appear in the lower frame, it is the filling task. You need to ignore the outer shape.
If the filling is two dots, you need to press B. 
If the filling is three dots, you need to press N. 

Press the SPACE BAR to see a recapitulative table with the stimulus.  
""", heading_size=80, heading_colour=BLACK, text_size=50, text_colour=BLACK)

# Run the experiment
instructions.present()
exp.keyboard.wait_char(" ")
reminder = stimuli.Picture("reminder.png")
reminder.present()
exp.keyboard.wait_char(" ")

for block in blocks:
    for trial in block.trials:
        exp.clock.wait(INTERTRIAL_DURATION)
        trial.stimuli[0].present()
        key, rt = exp.keyboard.wait_char([LOSANGE_OR_TWO_DOTS_KEY, SQUARE_OR_THREE_DOTS_KEY], duration=MAX_REP_DURATION)
        show_feedback(trial, key)

        exp.data.add([block.name,
            trial.get_factor("Task"),
            trial.get_factor("Form"),
            trial.get_factor("Dots"),
            key, rt])

control.end()