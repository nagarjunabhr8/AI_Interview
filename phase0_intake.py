#!/usr/bin/env python3
"""
PHASE 0 — INTAKE
Interview Agent: Collect candidate information before the interview begins.
Conversational, not rigid — but do not proceed until required items are collected.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional


class CandidateIntake:
    """Manages the intake process for interview candidates."""

    VALID_ROLES = [
        "QA Engineer", "Senior QA Engineer", "Lead QA Engineer", "QA Manager",
        "SDET", "Automation Architect", "Backend Developer", "DevOps Engineer",
        "Data Analyst", "Product Manager", "Frontend Engineer", "Full Stack Engineer",
        "Solutions Architect", "Tech Lead"
    ]

    VALID_SKILLS = [
        "Playwright", "Selenium", "Cypress", "Java", "JavaScript", "TypeScript",
        "Python", "C#", "RestAssured", "Cucumber", "BDD", "CI/CD", "Jenkins",
        "GitLab CI", "GitHub Actions", "Docker", "Kubernetes", "AWS", "Azure",
        "GCP", "Appium", "Machine Learning", "LLM Testing", "API Testing",
        "Performance Testing", "Security Testing", "Accessibility Testing",
        "Go", "Rust", "Node.js", "React", "Vue", "Angular"
    ]

    VALID_DIFFICULTY_LEVELS = ["Fresher", "Basic", "Simple", "Hard"]

    def __init__(self):
        """Initialize the intake collector."""
        self.candidate_data: Dict = {
            "role": None,
            "primary_skills": [],
            "years_of_experience": None,
            "difficulty_level": None,
            "resume": None,
            "self_ratings": {},
            "timestamp": datetime.now().isoformat()
        }
        self.intake_complete = False

    def clear_screen(self):
        """Clear console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        """Print welcome header."""
        print("\n" + "="*70)
        print("  AI INTERVIEW PANELIST — INTAKE PHASE")
        print("  Before we begin, let's gather some information about you.")
        print("="*70 + "\n")

    def get_role(self) -> str:
        """
        Collect target role / designation.
        Conversational approach with suggestions.
        """
        print("👤 STEP 1: TARGET ROLE")
        print("-" * 70)
        print("What role are you interviewing for?")
        print("\nExamples:")
        for i, role in enumerate(self.VALID_ROLES[:7], 1):
            print(f"  {i}. {role}")
        print(f"  ...and more\n")

        while True:
            role = input("Your target role: ").strip()
            if not role:
                print("❌ Please enter a role.\n")
                continue
            self.candidate_data["role"] = role
            print(f"✓ Got it — you're targeting: {role}\n")
            return role

    def get_primary_skills(self) -> List[str]:
        """
        Collect primary skill set(s).
        At least one required.
        """
        print("🛠️  STEP 2: PRIMARY SKILL SET(S)")
        print("-" * 70)
        print("What are your primary technical skills for this role?")
        print("(At least one required. Type them separated by commas.)\n")
        print("Examples: Playwright, Java, Python, Selenium, RestAssured, etc.\n")

        while True:
            skills_input = input("Your primary skills: ").strip()
            if not skills_input:
                print("❌ Please enter at least one skill.\n")
                continue

            skills = [s.strip() for s in skills_input.split(",")]
            if len(skills) == 0:
                print("❌ Please enter at least one skill.\n")
                continue

            self.candidate_data["primary_skills"] = skills
            print(f"✓ Skills captured: {', '.join(skills)}\n")
            return skills

    def get_years_of_experience(self) -> float:
        """
        Collect years of experience.
        Numeric input (e.g., 9.5 years).
        """
        print("📅 STEP 3: YEARS OF EXPERIENCE")
        print("-" * 70)
        print("How many years of experience do you have in this field?")
        print("(Enter as a number, e.g., 5, 9.5, 0.5)\n")

        while True:
            experience_input = input("Years of experience: ").strip()
            try:
                experience = float(experience_input)
                if experience < 0:
                    print("❌ Years of experience cannot be negative.\n")
                    continue
                self.candidate_data["years_of_experience"] = experience
                print(f"✓ Noted: {experience} years of experience\n")
                return experience
            except ValueError:
                print("❌ Please enter a valid number (e.g., 5 or 9.5).\n")

    def get_difficulty_level(self) -> str:
        """
        Collect interview difficulty level.
        One of: Fresher, Basic, Simple, Hard.
        """
        print("⚡ STEP 4: INTERVIEW DIFFICULTY LEVEL")
        print("-" * 70)
        print("What difficulty level suits you?")
        print()
        print("  1. Fresher       (0-1 yrs, fundamentals only, supportive)")
        print("  2. Basic         (definitions, 'what/how' questions)")
        print("  3. Simple        (moderate depth, 'why/when', comparisons)")
        print("  4. Hard          (scenario-based, architecture, trade-offs)")
        print()
        print("Not sure? Base it roughly on your years of experience:\n")

        years = self.candidate_data["years_of_experience"]
        if years <= 1:
            print("  (Your experience suggests: Fresher or Basic)")
        elif years <= 3:
            print("  (Your experience suggests: Basic or Simple)")
        elif years <= 6:
            print("  (Your experience suggests: Simple or Hard)")
        else:
            print("  (Your experience suggests: Hard)")
        print()

        while True:
            level_input = input("Choose level (Fresher/Basic/Simple/Hard): ").strip()
            if level_input not in self.VALID_DIFFICULTY_LEVELS:
                print(f"❌ Please choose from: {', '.join(self.VALID_DIFFICULTY_LEVELS)}\n")
                continue
            self.candidate_data["difficulty_level"] = level_input
            print(f"✓ Difficulty set to: {level_input}\n")
            return level_input

    def get_resume(self) -> Optional[str]:
        """
        Collect optional resume (paste as text).
        Will parse and extract technical skills and achievements.
        """
        print("📄 STEP 5: RESUME (OPTIONAL)")
        print("-" * 70)
        print("Do you have a resume you'd like to share?")
        print("(Paste it here, or press Enter twice to skip.)\n")
        print("To submit, press Enter twice:\n")

        lines = []
        empty_count = 0
        while True:
            line = input()
            if not line:
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
                lines.append(line)

        if lines:
            resume_text = "\n".join(lines).strip()
            if resume_text:
                self.candidate_data["resume"] = resume_text
                print(f"\n✓ Resume captured ({len(resume_text)} characters).\n")
                return resume_text

        print("✓ No resume provided — proceeding with self-reported skills.\n")
        return None

    def get_self_ratings(self) -> Dict[str, int]:
        """
        Collect self-ratings for key skills.
        Only ask for skills mentioned in primary_skills or resume.
        Scale 1-5.
        """
        print("⭐ STEP 6: SKILL SELF-RATINGS (OPTIONAL)")
        print("-" * 70)
        print("Rate your proficiency in each skill (1-5 scale):")
        print("  1 = Beginner  |  2 = Basic  |  3 = Intermediate")
        print("  4 = Advanced  |  5 = Expert\n")
        print("(Press Enter to skip a skill.)\n")

        skills_to_rate = self.candidate_data["primary_skills"]
        ratings = {}

        for skill in skills_to_rate:
            while True:
                rating_input = input(f"  {skill} (1-5): ").strip()
                if not rating_input:
                    break  # Skip this skill
                try:
                    rating = int(rating_input)
                    if 1 <= rating <= 5:
                        ratings[skill] = rating
                        break
                    else:
                        print(f"  ❌ Please enter a number between 1 and 5.")
                except ValueError:
                    print(f"  ❌ Please enter a valid number (1-5).")

        if "Test Automation Framework Design" in str(self.candidate_data.get("resume", "")):
            while True:
                rating_input = input(f"  Test Automation Framework Design (1-5): ").strip()
                if not rating_input:
                    break
                try:
                    rating = int(rating_input)
                    if 1 <= rating <= 5:
                        ratings["Test Automation Framework Design"] = rating
                        break
                    else:
                        print(f"  ❌ Please enter a number between 1 and 5.")
                except ValueError:
                    print(f"  ❌ Please enter a valid number (1-5).")

        self.candidate_data["self_ratings"] = ratings
        if ratings:
            print(f"\n✓ Ratings captured: {ratings}\n")
        else:
            print("✓ Proceeding without detailed skill ratings.\n")
        return ratings

    def confirm_intake(self) -> bool:
        """
        Display intake summary and ask for confirmation.
        """
        print("\n" + "="*70)
        print("  INTAKE SUMMARY")
        print("="*70 + "\n")

        print(f"Role:                    {self.candidate_data['role']}")
        print(f"Primary Skills:          {', '.join(self.candidate_data['primary_skills'])}")
        print(f"Years of Experience:     {self.candidate_data['years_of_experience']}")
        print(f"Difficulty Level:        {self.candidate_data['difficulty_level']}")
        print(f"Resume Provided:         {'Yes' if self.candidate_data['resume'] else 'No'}")

        if self.candidate_data['self_ratings']:
            print(f"Self-Ratings:")
            for skill, rating in self.candidate_data['self_ratings'].items():
                print(f"  - {skill}: {rating}/5")

        # Calculate expected question count and duration
        years = self.candidate_data['years_of_experience']
        difficulty = self.candidate_data['difficulty_level']

        if difficulty in ["Fresher", "Basic"]:
            question_count = "15-20"
        elif difficulty == "Simple":
            question_count = "20-25"
        else:  # Hard
            question_count = "25-30"

        print(f"\nInterview Plan:")
        print(f"  • Approximately {question_count} questions")
        print(f"  • Expected duration: ~45 minutes")
        print(f"  • Topics: Core fundamentals, skills deep-dive, coding,")
        print(f"    automation/framework, and scenario-based questions")

        print("\n" + "-"*70)
        proceed = input("\nReady to start the interview? (yes/no): ").strip().lower()

        if proceed in ["yes", "y"]:
            self.intake_complete = True
            print("\n✓ Intake complete! Starting interview...\n")
            return True
        else:
            print("\n❌ Intake cancelled. Let's review and try again.\n")
            return False

    def run(self) -> Dict:
        """
        Run the full intake process.
        Returns candidate data dictionary.
        """
        self.clear_screen()
        self.print_header()

        # Collect required information
        self.get_role()
        self.get_primary_skills()
        self.get_years_of_experience()
        self.get_difficulty_level()
        self.get_resume()
        self.get_self_ratings()

        # Confirm before proceeding
        while not self.confirm_intake():
            print("\nLet's re-enter your information.\n")
            self.candidate_data = {
                "role": None,
                "primary_skills": [],
                "years_of_experience": None,
                "difficulty_level": None,
                "resume": None,
                "self_ratings": {},
                "timestamp": datetime.now().isoformat()
            }
            self.get_role()
            self.get_primary_skills()
            self.get_years_of_experience()
            self.get_difficulty_level()
            self.get_resume()
            self.get_self_ratings()

        return self.candidate_data

    def save_to_file(self, filename: str = "candidate_intake.json"):
        """Save candidate intake data to JSON file."""
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'w') as f:
            json.dump(self.candidate_data, f, indent=2)
        print(f"✓ Candidate data saved to: {filename}")
        return filepath


def main():
    """Entry point for the intake phase."""
    intake = CandidateIntake()
    candidate_data = intake.run()

    # Save to file for Phase 1 to use
    intake.save_to_file()

    print("="*70)
    print("INTAKE PHASE COMPLETE")
    print("="*70)
    print(f"\nCandidate: {candidate_data['role']}")
    print(f"Skills: {', '.join(candidate_data['primary_skills'])}")
    print(f"Experience: {candidate_data['years_of_experience']} years")
    print(f"Level: {candidate_data['difficulty_level']}")
    print("\nReady for Phase 1 — Interview Execution")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
