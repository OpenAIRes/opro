import os
import pickle
import pyperclip
import sys

meta_prompt = (
    "Your task is to generate the instruction <INS>."
    " Below are some previous instructions with their scores."
    " The score ranges from 0 to 100.\n"
)

new = False  # Set to False if you want to load existing results

if new:
  results_dict = dict()
  results_dict["old_instructions_and_scores"] = list([["", 0]])
  save_folder = "results"
  with open(os.path.join(save_folder, "results_dict.pkl"), "wb") as fp:
    pickle.dump(results_dict, fp)

with open("results/results_dict.pkl", "rb") as fp:
  results_dict = pickle.load(fp)
old_instructions_and_scores = results_dict["old_instructions_and_scores"]
for instruction, score in old_instructions_and_scores:
  meta_prompt += (
      f"\ntext:\n{instruction}\nscore:\n{score}\n"
  )

meta_prompt += (
    "\n\nGenerate an instruction that"
    " is different from all the instructions <INS> above,"
    " and has a higher score than all the instructions <INS> above."
    " The instruction should begin with <INS> and end with </INS>."
)

pyperclip.copy(meta_prompt)  # This copies the string to the clipboard
print("Prompt copied to clipboard.")

print("Enter the new instruction (finish with Ctrl+Z then Enter):")
instruction = sys.stdin.read()
score = int(input("Enter the score for the new instruction (0-100): "))
old_instructions_and_scores.append([instruction, score])
old_instructions_and_scores = sorted(
    old_instructions_and_scores, key=lambda x: x[1]
)
results_dict["old_instructions_and_scores"] = old_instructions_and_scores
with open("results/results_dict.pkl", "wb") as fp:
    pickle.dump(results_dict, fp)

