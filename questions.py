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

    #TRUST
        ["T1_F", "radio_text", "The drone’s behaviour was predictable",["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        ["T2_F", "radio_text", "The drone was capable of sensing my emotions",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        
        
        ["T3_F", "radio_text", "I could count on the drone to do its job", ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"]],
        ["T4_F", "radio_text", "Piloting the drone was enjoyable",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],




        ["T5_F", "radio_text", "The drone would be able to cope with similar tasks in the future",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        ["T6_F", "radio_text", "I was satisfied with the level of control I had whilst piloting the drone",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],




        ["T7_F", "radio_text", "Overall, I trust the drone",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        ["T8_F", "radio_text", "I would be willing to fly this drone again in the future",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        ["T9_F", "radio_text", "The drone's behaviour was reliable",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],


        ["T1_NF", "radio_text", "The drone’s behaviour was predictable",["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        ["T2_NF", "radio_text", "The drone was capable of sensing my emotions",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        
        
        ["T3_NF", "radio_text", "I could count on the drone to do its job", ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"]],
        ["T4_NF", "radio_text", "Piloting the drone was enjoyable",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],




        ["T5_NF", "radio_text", "The drone would be able to cope with similar tasks in the future",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        ["T6_NF", "radio_text", "I was satisfied with the level of control I had whilst piloting the drone",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],




        ["T7_NF", "radio_text", "Overall, I trust the drone",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        ["T8_NF", "radio_text", "I would be willing to fly this drone again in the future",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],
        ["T9_NF", "radio_text", "The drone's behaviour was reliable",    ["1", "2", "3", "4", "5","6","7"], ["Strongly Disagree", "Strongly Agree"] ],

    
]

# Unused, questions are randomized
QUESTION_ORDER = {

        "E1_": 1,
        "E2_": 2,
        "E3_": 3,
        "AA1_": 4,
        "AA2_": 5,
        "AA3_": 6,
        "AA4_": 7,
        "AE1_": 8,
        "AE2_": 9,
        "AE3_": 10,
        "IQ1_": 11,
        "IQ2_": 12,
        "IQ3_": 13,
        "P1_": 14,
        "P2_": 15
    

}
