# Motivation.com
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=50&duration=1500&pause=2000&color=20F77B&width=1500&height=100&lines=WrongThinkingIsOnlyProblemInLife;RightThinkingIsOnlySolutionToAllOurProblems;SelflessnessIsTheOnlyWayToProgressAndProsperity;EveryActCanBeAnActOfPrayer;ConectToHigerConciousnessDaily;LiveWhatYouLearn;NeverGiveUpOnYourself;ValueYourBlessings;SeeDivinityAllAround;AbsorbYourMindIntoHigher;DetachFromMayaAndAttachToDivine;GiveProsperityToDivinity;BeingGoodIsAnRewardInItself">


// ==============================================
// 🚀 MOTIVATIONAL JS - Console Inspiration Boost 🚀
// ==============================================
// Paste this in your project for daily motivation!
// Displays random inspiring messages in console.

function motivateMe() {
  const quotes = [
    "🚀 Your code is changing the world!",
    "💡 Every bug you fix makes you a better developer.",
    "🔥 You're one step closer to your goals!",
    "🌟 Believe in your code, and others will too.",
    "👩‍💻 Keep coding. The world needs your ideas!",
    "🎯 Success is just a function of persistence.",
    "⚡ Debugging is where the real learning happens.",
    "🚧 Obstacles are just opportunities in disguise.",
    "🌈 Your next breakthrough is just a commit away!",
    "🎉 Celebrate every small victory!",
    "💪 You're capable of more than you know!",
    "🧠 Growth happens outside your comfort zone!",
    "✨ The best developers were once beginners too!",
    "🛠️ Your skills are tools - keep sharpening them!",
    "⏳ Time invested in learning is never wasted!"
  ];
  
  const randomIndex = Math.floor(Math.random() * quotes.length);
  const randomQuote = quotes[randomIndex];
  
  // Style the console output
  const styles = [
    "color: #4CAF50",  // Green text
    "font-size: 16px",
    "font-weight: bold",
    "padding: 10px",
    "border: 2px solid #4CAF50",
    "border-radius: 5px",
    "background: #f8f8f8"
  ].join(";");
  
  console.log(`%c${randomQuote}`, styles);
}

// Run immediately
motivateMe();

// Optional: Run on page load in browser
if (typeof window !== 'undefined') {
  window.addEventListener('load', motivateMe);
}

// Optional: Run every hour (3600000ms)
// setInterval(motivateMe, 3600000);
