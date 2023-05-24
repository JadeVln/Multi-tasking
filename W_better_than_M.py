
from expyriment import design, control, stimuli
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

instructions = expyriment.stimuli.TextScreen("Instructions", f"""Lorem Ipsum""")
blankscreen = stimuli.BlankScreen()

exp = design.Experiment(name=" Multitasking Experiment", background_colour = GREY, text_size=40)
#control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment
control.defaults.auto_create_subject_id = True
control.defaults.initialize_delay = 5


control.initialize(exp)

control.start()

#Associte W and H to the size of the screen 
W, H = exp.screen.window_size 

#Create rectangle frame and labels 
frame = stimuli.Rectangle((.6*W, .8*H), colour=BLACK, line_width=10)
line = stimuli.Line((-.3*W, 0), (.3*W, 0), colour=BLACK, line_width=10)
label_top = stimuli.TextLine("Shape", position= (0, 0.45*H), text_size=80, text_colour=BLACK)  
label_bottom = stimuli.TextLine("Filling", position=(0, -0.45*H), text_size=80, text_colour=BLACK) 


#Load all the stimuli images into variables 
square_2u = stimuli.Picture("square_2.png")
square_2d = stimuli.Picture("square_2.png")
square_3u = stimuli.Picture("square_3.png")
square_3d = stimuli.Picture("square_3.png")
losange_2u = stimuli.Picture("losange_2.png")
losange_2d = stimuli.Picture("losange_2.png")
losange_3u = stimuli.Picture("losange_3.png")
losange_3d = stimuli.Picture("losange_3.png")

#Stimuli Square 2 dots up 
square_2u.reposition((0, 0.2*H))
square_2u.scale((.7, .7))

canvas_s2u= stimuli.Canvas((W, H))

square_2u.plot(canvas_s2u)
frame.plot(canvas_s2u)
line.plot(canvas_s2u)
label_top.plot(canvas_s2u)
label_bottom.plot(canvas_s2u)


#Stimuli Square 2 dots down
square_2d.reposition((0, -0.2*H))
square_2d.scale((.7, .7))

canvas_s2d= stimuli.Canvas((W, H))

square_2d.plot(canvas_s2d)
frame.plot(canvas_s2d)
line.plot(canvas_s2d)
label_top.plot(canvas_s2d)
label_bottom.plot(canvas_s2d)

#Stimuli Square 3 dots up 
square_3u.reposition((0, 0.2*H))
square_3u.scale((.7, .7))

canvas_s3u= stimuli.Canvas((W, H))

square_3u.plot(canvas_s3u)
frame.plot(canvas_s3u)
line.plot(canvas_s3u)
label_top.plot(canvas_s3u)
label_bottom.plot(canvas_s3u)

#Stimuli Square 3 dots down 
square_3d.reposition((0, -0.2*H))
square_3d.scale((.7, .7))

canvas_s3d= stimuli.Canvas((W, H))

square_3d.plot(canvas_s3d)
frame.plot(canvas_s3d)
line.plot(canvas_s3d)
label_top.plot(canvas_s3d)
label_bottom.plot(canvas_s3d)

#Stimuli Losange 2 dots up 
losange_2u.reposition((0, 0.2*H))
losange_2u.scale((.7, .7))

canvas_l2u= stimuli.Canvas((W, H))

losange_2u.plot(canvas_l2u)
frame.plot(canvas_l2u)
line.plot(canvas_l2u)
label_top.plot(canvas_l2u)
label_bottom.plot(canvas_l2u)

#Stimuli Losange 2 dots down 
losange_2d.reposition((0, -0.2*H))
losange_2d.scale((.7, .7))

canvas_l2d= stimuli.Canvas((W, H))

losange_2d.plot(canvas_l2d)
frame.plot(canvas_l2d)
line.plot(canvas_l2d)
label_top.plot(canvas_l2d)
label_bottom.plot(canvas_l2d)

#Stimuli Losange 3 dots up  
losange_3u.reposition((0, 0.2*H))
losange_3u.scale((.7, .7))

canvas_l3u= stimuli.Canvas((W, H))

losange_3u.plot(canvas_l3u)
frame.plot(canvas_l3u)
line.plot(canvas_l3u)
label_top.plot(canvas_l3u)
label_bottom.plot(canvas_l3u)

#Stimuli Losange 3 dots down  
losange_3d.reposition((0, -0.2*H))
losange_3d.scale((.7, .7))

canvas_l3d= stimuli.Canvas((W, H))

losange_3d.plot(canvas_l3d)
frame.plot(canvas_l3d)
line.plot(canvas_l3d)
label_top.plot(canvas_l3d)
label_bottom.plot(canvas_l3d)


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

shape_block_t = design.Block(name="Shape Task Training Block")
for _ in range(TRAINING_TRIALS_PER_BLOCK):  # Number of trials per block
    trial = design.Trial()
        
    # Randomly choose betweent congruent and incongruent stimuli for the trial
    is_congruent = random.choice([True, False]) #Proba 0.5 : True (congruent) and False (incongruent)

    if is_congruent :     
        stimulus = design.randomize.rand_element(stimuli_shape_c)
    else : 
        stimulus = design.randomize.rand_element(stimuli_shape_in)

    trial.add_stimulus(stimulus)
    shape_block_t.add_trial(trial)
        
blocks.append(shape_block_t)


filling_block_t = design.Block(name="Filling Task Training Block")
for _ in range(TRAINING_TRIALS_PER_BLOCK):  # Number of trials per block
    trial = design.Trial()
        
    # Randomly choose betweent congruent and incongruent stimuli for the trial
    is_congruent = random.choice([True, False]) #Proba 0.5 : True (congruent) and False (incongruent)

    if is_congruent :     
        stimulus = design.randomize.rand_element(stimuli_filling_c)
    else : 
        stimulus = design.randomize.rand_element(stimuli_filling_in)
    
    trial.add_stimulus(stimulus)
    filling_block_t.add_trial(trial)
        
blocks.append(filling_block_t)


mixed_block_t = design.Block(name="Mixed Task Block")
for _ in range(TRAINING_TRIALS_PER_BLOCK):  # Number of trials per block
    trial = design.Trial()

    # Randomly choose betweent congruent and incongruent stimuli for the trial
    is_congruent = random.choice([True, False]) #Proba 0.5 : True (congruent) and False (incongruent)

    if is_congruent :     
        stimulus = design.randomize.rand_element(stimuli_c)
    else : 
        stimulus = design.randomize.rand_element(stimuli_in)

    trial.add_stimulus(stimulus)
    mixed_block_t.add_trial(trial)
        
blocks.append(mixed_block_t)


shape_block_a = design.Block(name="Shape Task Block")
for _ in range(TRIALS_PER_BLOCK):  # Number of trials per block
    trial = design.Trial()

    # Randomly choose betweent congruent and incongruent stimuli for the trial
    is_congruent = random.choice([True, False]) #Proba 0.5 : True (congruent) and False (incongruent)

    if is_congruent :     
        stimulus = design.randomize.rand_element(stimuli_shape_c)
    else : 
        stimulus = design.randomize.rand_element(stimuli_shape_in)
    trial.add_stimulus(stimulus)
    shape_block_a.add_trial(trial)
        
blocks.append(shape_block_a)


filling_block_a = design.Block(name="Filling Task Block")
for _ in range(TRIALS_PER_BLOCK):  # Number of trials per block
    trial = design.Trial()
        
    # Randomly choose betweent congruent and incongruent stimuli for the trial
    is_congruent = random.choice([True, False]) #Proba 0.5 : True (congruent) and False (incongruent)

    if is_congruent :     
        stimulus = design.randomize.rand_element(stimuli_filling_c)
    else : 
        stimulus = design.randomize.rand_element(stimuli_filling_in)
    
    trial.add_stimulus(stimulus)
    filling_block_a.add_trial(trial)
        
blocks.append(filling_block_a)


mixed_block_a = design.Block(name="Mixed Task Block")
for _ in range(TRAINING_TRIALS_PER_BLOCK):  # Number of trials per block
    trial = design.Trial()

    # Randomly choose betweent congruent and incongruent stimuli for the trial
    is_congruent = random.choice([True, False]) #Proba 0.5 : True (congruent) and False (incongruent)

    if is_congruent :     
        stimulus = design.randomize.rand_element(stimuli_c)
    else : 
        stimulus = design.randomize.rand_element(stimuli_in)
    
    # Present stimuli and collect responses
    trial.add_stimulus(stimulus)
    mixed_block_a.add_trial(trial)
        
blocks.append(mixed_block_a)


#Create list of stimuli for the feedback message

LOSANGE_OR_TWO_DOTS = [canvas_l2u, canvas_l3d, canvas_l2d, canvas_l3u, canvas_s2d, canvas_s2u]
SQUARE_OR_THREE_DOTS = [canvas_s2u, canvas_s3d, canvas_s2d, canvas_s3u, canvas_l2d, canvas_l2u]

# Feedback message function
def show_feedback(trial):
    stimulus = trial.stimuli[0]
    REMINDER_KEY_STIMULUS = False

    if key == None : 
        feedback_text = 'Time is up'
        REMINDER_KEY_STIMULUS = True 
    else : 
        if stimulus in LOSANGE_OR_TWO_DOTS : 
            if key !=  LOSANGE_OR_TWO_DOTS_KEY : 
                feedback_text = "That was the wrong key"
                REMINDER_KEY_STIMULUS = True 
        elif stimulus in SQUARE_OR_THREE_DOTS : 
            if key != SQUARE_OR_THREE_DOTS_KEY : 
                feedback_text = "That was the wrong key"
                REMINDER_KEY_STIMULUS = True 

    feedback = stimuli.TextLine(feedback_text, position=(0, 0), text_size=60, text_colour=BLACK)
    feedback.present()
    exp.clock.wait(1000)  # Display feedback for 1 second
    feedback.unload()

    if REMINDER_KEY_STIMULUS == True : 
        reminder = stimuli.Picture("reminder.png"), (0, 0)
        reminder.present()
        exp.clock.wait(5000)  # Display reminder for 5 seconds
        reminder.unload()
        blankscreen.present()
        exp.clock.wait(500)



exp.add_data_variable_names(['Respkey', 'RT'])

#Run the experiment 
#control.start(exp)

instructions.present()
exp.keyboard.wait_char(" ")

for block in blocks:
    for trial in block.trials:
        blankscreen.present()
        exp.clock.wait(INTERTRIAL_DURATION)
        trial.stimuli[0].present()

        key, rt = exp.keyboard.wait_char([LOSANGE_OR_TWO_DOTS_KEY, SQUARE_OR_THREE_DOTS_KEY], duration=MAX_REP_DURATION)
        
        show_feedback(trial)


# Save data
exp.data.add([key, rt])
exp.data.rename("multitasking_data")
exp.data.save("multitasking_data.csv")


control.end()
