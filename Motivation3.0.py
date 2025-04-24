import random
import json
import datetime
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
from textblob import TextBlob  # Requires installation: pip install textblob

class MomentumX:
    def __init__(self, user_name: str):
        self.user_name = user_name
        self.start_date = datetime.datetime.now()
        self.habits = {}
        self.motivational_level = 50  # 0-100 scale
        self.performance_history = []
        self.nlp_responses = self._load_nlp_responses()
        self.quote_db = self._load_quotes()
        
    def _load_nlp_responses(self) -> Dict[str, List[str]]:
        """Load dynamic response templates"""
        return {
            "positive": [
                "Your progress is remarkable, {name}! The compound effect is working.",
                "This momentum is exactly what we predicted in Phase 2, {name}. Keep going!",
                "You're demonstrating textbook high-performer behavior today!"
            ],
            "neutral": [
                "Consistency beats intensity, {name}. Stay the course.",
                "This is where growth happens - right outside your comfort zone."
            ],
            "negative": [
                "Temporary setbacks are data points, {name}. Let's analyze and adjust.",
                "The obstacle is the way. What's one micro-action you can take right now?"
            ]
        }
    
    def _load_quotes(self) -> List[str]:
        """Database of motivational quotes"""
        return [
            "Discipline is choosing between what you want now and what you want most.",
            "You don't have to be great to start, but you have to start to be great.",
            "The only limit to our realization of tomorrow is our doubts of today."
        ]
    
    def add_habit(self, habit_name: str, difficulty: int):
        """Register a new habit with tracking"""
        self.habits[habit_name] = {
            "streak": 0,
            "max_streak": 0,
            "difficulty": difficulty,
            "history": []
        }
    
    def log_habit(self, habit_name: str, sentiment_analysis: Optional[str] = None):
        """Record habit completion with optional journaling"""
        if habit_name not in self.habits:
            raise ValueError(f"Habit {habit_name} not registered")
        
        self.habits[habit_name]["streak"] += 1
        if self.habits[habit_name]["streak"] > self.habits[habit_name]["max_streak"]:
            self.habits[habit_name]["max_streak"] = self.habits[habit_name]["streak"]
        
        entry = {
            "date": datetime.datetime.now().isoformat(),
            "streak": self.habits[habit_name]["streak"],
            "sentiment": self._analyze_sentiment(sentiment_analysis) if sentiment_analysis else None
        }
        self.habits[habit_name]["history"].append(entry)
        self._update_motivation(habit_name)
        
    def _analyze_sentiment(self, text: str) -> float:
        """NLP sentiment analysis (-1 to 1 scale)"""
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
    
    def _update_motivation(self, habit_name: str):
        """Dynamic motivation adjustment algorithm"""
        habit = self.habits[habit_name]
        streak_boost = min(habit["streak"] * 0.5, 15)
        difficulty_boost = habit["difficulty"] * 0.3
        
        # Non-linear motivation growth curve
        self.motivational_level = min(
            self.motivational_level + streak_boost + difficulty_boost,
            100
        )
        self.performance_history.append(
            (datetime.datetime.now(), self.motivational_level)
        )
    
    def get_feedback(self) -> str:
        """Personalized NLP coaching response"""
        if not self.performance_history:
            return random.choice(self.nlp_responses["neutral"]).format(name=self.user_name)
        
        last_week = [x[1] for x in self.performance_history 
                    if (datetime.datetime.now() - x[0]).days <= 7]
        
        if not last_week:
            trend = 0
        else:
            trend = (last_week[-1] - last_week[0]) / len(last_week)
        
        if trend > 1.5:
            return random.choice(self.nlp_responses["positive"]).format(name=self.user_name)
        elif trend < -1:
            return random.choice(self.nlp_responses["negative"]).format(name=self.user_name)
        else:
            return random.choice(self.nlp_responses["neutral"]).format(name=self.user_name)
    
    def generate_motivational_quote(self) -> str:
        """Context-aware quote generation"""
        streaks = [h["streak"] for h in self.habits.values()]
        if streaks and max(streaks) >= 7:
            return "🔥 " + random.choice([
                "Your consistency is creating inevitable success!",
                "The compound effect is working in your favor - keep stacking days!"
            ])
        return random.choice(self.quote_db)
    
    def visualize_progress(self):
        """Generate matplotlib progress charts"""
        if not self.performance_history:
            print("No data to visualize yet!")
            return
            
        dates = [x[0] for x in self.performance_history]
        levels = [x[1] for x in self.performance_history]
        
        plt.figure(figsize=(10, 5))
        plt.plot(dates, levels, 'b-', marker='o')
        plt.title(f"{self.user_name}'s Motivation Trajectory")
        plt.xlabel("Date")
        plt.ylabel("Motivation Level (0-100)")
        plt.grid(True)
        plt.show()
        
        # Habit streak visualization
        if self.habits:
            plt.figure(figsize=(10, 5))
            habits = list(self.habits.keys())
            streaks = [self.habits[h]["streak"] for h in habits]
            plt.bar(habits, streaks)
            plt.title("Current Habit Streaks")
            plt.ylabel("Days")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

# Example Usage
if __name__ == "__main__":
    program = MomentumX("Alex")
    
    # Register habits
    program.add_habit("Morning Meditation", difficulty=3)
    program.add_habit("Workout", difficulty=5)
    program.add_habit("Learning Session", difficulty=4)
    
    # Simulate 2 weeks of tracking
    for day in range(14):
        for habit in program.habits:
            # Random completion for demo (real usage would get user input)
            if random.random() > 0.3:  # 70% completion rate
                journal = "Feeling good about this" if random.random() > 0.5 else "Tough but worth it"
                program.log_habit(habit, journal)
        
        # Daily feedback
        print(f"\nDay {day + 1}: {program.generate_motivational_quote()}")
        print(f"Coach Feedback: {program.get_feedback()}")
    
    # Visualize progress
    program.visualize_progress()
