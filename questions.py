# list of questions.
# ## Each questions is a list: 0: UID, 1: title, 2: response options
# QUESTIONS = {

#     1: [    ["Q01", "radio_text", "Multiple choice question", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q02", "radio_img", "Multiple choice with emoji tho (or pics)", ["1", "2","3", "4", "5"]],
#             ["Q03", "open_text", "Text response", [None]],
#     ],
#     2: [    ["Q11", "radio_text", "Did the robot move in an acceptable way?", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q12", "radio_text", "Did the robot move as you would have expected?", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q13", "radio_img", "Emoji Response", ["1", "2","3", "4", "5"]],
#             ["Q14", "radio_text", "Did the robot move in an acceptable way?", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q15", "radio_img", "What was the robot's task", ["artichoke", "basket","sandtimer"]]
#     ]
    
QUESTIONS = [

    #Enjoyment
        ["F1", "radio_text",  "To what extent can the drone's behavior be predicted from moment to moment?",["1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"]  ],
        ["F2", "radio_text", "I felt that the drone was capable of sensing my emotions",    ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Very capable"] ],
        
        
        ["F3", "radio_text", "To what extent can you count on the drone to do its job?", ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"]],
        ["F4", "radio_text", "I felt piloting the drone was enjoyable",    ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Very enjoyable"] ],




        ["F5", "radio_text", "What degree of faith do you have that the drone will be able to cope with similar situations in the future?",    ["1", "2", "3", "4", "5","6","7"], ["Not faith at all", "Complete faith"] ],
        ["F6", "radio_text", "How satisfied were you with the level of control you had while flying the quadcopter drone?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Very satisfied"]  ],




        ["F7", "radio_text", "Overall how much do you trust the drone?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Very much"] ],
        ["F8", "radio_text", "Considering your overall experience, how likely are you to fly a quadcopter drone again in the future?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Very likely"] ],
        

]

# Unused, questions are randomized
QUESTION_ORDER = {

        "E1_": 1,
        "E2_": 2,
        "E3_": 3
    

}
