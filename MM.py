import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html>
<head>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useEffect } = React;

        // Icon Components 추가
        const Trophy = ({ className }) => (
            <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                />
            </svg>
        );

        const Star = ({ className }) => (
            <svg className={className} fill="currentColor" stroke="currentColor" viewBox="0 0 24 24">
                <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
                />
            </svg>
        );
    const Gift = ({ className }) => (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v13m0-13V6a2 2 0 112 2h-2zm0 0V5.5A2.5 2.5 0 109.5 8H12zm-7 4h14M5 12a2 2 0 110-4h14a2 2 0 110 4M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7" />
    </svg>
);

const Flame = ({ className }) => (
    <svg className={className} fill="currentColor" viewBox="0 0 24 24">
        <path d="M12 2c1.5 3.5 3 6 3 9 0 3-2 5-5 5s-5-2-5-5c0-3 1.5-5.5 3-9 1 2 2.5 4 4 6z" />
    </svg>
);

const Unlock = ({ className }) => (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 11V7a4 4 0 118 0m-4 8v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2z" />
    </svg>
);

const Lock = ({ className }) => (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
    </svg>
);

const Heart = ({ className }) => (
    <svg className={className} fill="currentColor" viewBox="0 0 24 24">
        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
    </svg>
);

const Clock = ({ className }) => (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
);

const Target = ({ className }) => (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <circle cx="12" cy="12" r="10" strokeWidth={2} />
        <circle cx="12" cy="12" r="6" strokeWidth={2} />
        <circle cx="12" cy="12" r="2" fill="currentColor" />
    </svg>
);

const Brain = ({ className }) => (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
    </svg>
);

const Zap = ({ className }) => (
    <svg className={className} fill="currentColor" viewBox="0 0 24 24">
        <path d="M13 2L3 14h8l-1 8 10-12h-8l1-8z" />
    </svg>
);

const CheckCircle = ({ className }) => (
    <svg className={className} fill="currentColor" viewBox="0 0 24 24">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" />
    </svg>
);

const XCircle = ({ className }) => (
    <svg className={className} fill="currentColor" viewBox="0 0 24 24">
        <path d="M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2zm5 13.59L15.59 17 12 13.41 8.41 17 7 15.59 10.59 12 7 8.41 8.41 7 12 10.59 15.59 7 17 8.41 13.41 12 17 15.59z" />
    </svg>
);

const RefreshCw = ({ className }) => (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
    </svg>
);

const TrendingUp = ({ className }) => (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
    </svg>
);

const Award = ({ className }) => (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <circle cx="12" cy="8" r="7" strokeWidth={2} />
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8.21 13.89L7 23l5-3 5 3-1.21-9.11" />
    </svg>
);
        

     
    </script>
</body>
</html>

const MultiplicationMasterGame = () => {
  const [currentLevel, setCurrentLevel] = useState(1);
  const [totalStars, setTotalStars] = useState(0);
  const [totalMoney, setTotalMoney] = useState(0);
  const [unlockedLevels, setUnlockedLevels] = useState([1]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3);
  const [streak, setStreak] = useState(0);
  const [maxStreak, setMaxStreak] = useState(0);
  const [selected, setSelected] = useState(null);
  const [isCorrect, setIsCorrect] = useState(null);
  const [showHint, setShowHint] = useState(false);
  const [timeLeft, setTimeLeft] = useState(30);
  const [isPlaying, setIsPlaying] = useState(false);
  const [gameMode, setGameMode] = useState('menu');
  const [levelStars, setLevelStars] = useState(0);
  const [hintUsed, setHintUsed] = useState(false);

  const levels = {
    1: {
      name: "기본 곱셈공식",
      difficulty: "쉬움",
      reward: 100,
      questions: [
        {
          question: "(a + b)² = ?",
          answer: "a² + 2ab + b²",
          hint: "앞제곱 + 2×앞×뒤 + 뒤제곱",
          options: ["a² + 2ab + b²", "a² + ab + b²", "a² + b²", "2a² + 2b²"]
        },
        {
          question: "(a - b)² = ?",
          answer: "a² - 2ab + b²",
          hint: "앞제곱 - 2×앞×뒤 + 뒤제곱",
          options: ["a² - 2ab + b²", "a² - ab + b²", "a² - b²", "a² + 2ab - b²"]
        },
        {
          question: "(a + b)(a - b) = ?",
          answer: "a² - b²",
          hint: "합차공식: 앞제곱 - 뒤제곱",
          options: ["a² - b²", "a² + b²", "2ab", "a² - 2ab + b²"]
        },
        {
          question: "(x + 3)² = ?",
          answer: "x² + 6x + 9",
          hint: "(a + b)² 공식 적용",
          options: ["x² + 6x + 9", "x² + 3x + 9", "x² + 9", "x² + 3x + 6"]
        },
        {
          question: "(2x - 1)² = ?",
          answer: "4x² - 4x + 1",
          hint: "(a - b)² 공식에서 a=2x, b=1",
          options: ["4x² - 4x + 1", "4x² - 2x + 1", "2x² - 4x + 1", "4x² - 1"]
        }
      ]
    },
    2: {
      name: "중급 곱셈공식",
      difficulty: "보통",
      reward: 150,
      questions: [
        {
          question: "(x + a)(x + b) = ?",
          answer: "x² + (a+b)x + ab",
          hint: "십자가 곱셈법",
          options: ["x² + (a+b)x + ab", "x² + ax + bx", "x² + ab", "x² + 2ab"]
        },
        {
          question: "(2x + 3)(x + 5) = ?",
          answer: "2x² + 13x + 15",
          hint: "앞×앞, 겉×속+속×겉, 뒤×뒤",
          options: ["2x² + 13x + 15", "2x² + 8x + 15", "2x² + 10x + 15", "2x² + 15x + 13"]
        },
        {
          question: "(a + b + c)² = ?",
          answer: "a² + b² + c² + 2ab + 2bc + 2ca",
          hint: "각 항의 제곱 + 2×모든 조합",
          options: [
            "a² + b² + c² + 2ab + 2bc + 2ca",
            "a² + b² + c²",
            "a² + b² + c² + ab + bc + ca",
            "(a+b+c)²"
          ]
        },
        {
          question: "(3x - 2)(2x + 5) = ?",
          answer: "6x² + 11x - 10",
          hint: "3×2=6, 3×5+(-2)×2=11, (-2)×5=-10",
          options: ["6x² + 11x - 10", "6x² + 15x - 10", "6x² - 10", "5x² + 11x - 10"]
        },
        {
          question: "(x + 2)(x - 3) = ?",
          answer: "x² - x - 6",
          hint: "십자가 곱셈: 2+(-3)=-1, 2×(-3)=-6",
          options: ["x² - x - 6", "x² + x - 6", "x² - 6", "x² - 5x - 6"]
        }
      ]
    },
    3: {
      name: "고급 곱셈공식",
      difficulty: "어려움",
      reward: 200,
      questions: [
        {
          question: "(a + b)³ = ?",
          answer: "a³ + 3a²b + 3ab² + b³",
          hint: "계수: 1, 3, 3, 1 (파스칼 삼각형)",
          options: [
            "a³ + 3a²b + 3ab² + b³",
            "a³ + b³",
            "a³ + 2a²b + 2ab² + b³",
            "a³ + a²b + ab² + b³"
          ]
        },
        {
          question: "(a - b)³ = ?",
          answer: "a³ - 3a²b + 3ab² - b³",
          hint: "계수: 1, -3, 3, -1 (부호 교대)",
          options: [
            "a³ - 3a²b + 3ab² - b³",
            "a³ - b³",
            "a³ - 2a²b + 2ab² - b³",
            "a³ + 3a²b - 3ab² - b³"
          ]
        },
        {
          question: "(a + b)(a² - ab + b²) = ?",
          answer: "a³ + b³",
          hint: "세제곱의 합 공식",
          options: ["a³ + b³", "a³ - b³", "a² + b²", "a³ + 3ab + b³"]
        },
        {
          question: "(a - b)(a² + ab + b²) = ?",
          answer: "a³ - b³",
          hint: "세제곱의 차 공식",
          options: ["a³ - b³", "a³ + b³", "a² - b²", "a³ - 3ab - b³"]
        },
        {
          question: "(x + 1)³ = ?",
          answer: "x³ + 3x² + 3x + 1",
          hint: "(a+b)³ 공식에 b=1 대입",
          options: ["x³ + 3x² + 3x + 1", "x³ + 1", "x³ + x² + x + 1", "x³ + 3x + 1"]
        }
      ]
    },
    4: {
      name: "곱셈공식 변형 - 기본",
      difficulty: "보통",
      reward: 150,
      questions: [
        {
          question: "a² + b² = (a+b)² - ?",
          answer: "2ab",
          hint: "(a+b)² = a² + 2ab + b²에서 유도",
          options: ["2ab", "ab", "a²b²", "4ab"]
        },
        {
          question: "a² + b² = (a-b)² + ?",
          answer: "2ab",
          hint: "(a-b)² = a² - 2ab + b²에서 유도",
          options: ["2ab", "ab", "-2ab", "4ab"]
        },
        {
          question: "(a+b)² - (a-b)² = ?",
          answer: "4ab",
          hint: "전개해서 빼면",
          options: ["4ab", "2ab", "2a²", "2b²"]
        },
        {
          question: "a²+b² = 25, ab = 12일 때, (a+b)² = ?",
          answer: "49",
          hint: "(a+b)² = a² + 2ab + b²",
          options: ["49", "61", "37", "25"]
        },
        {
          question: "a+b = 5, ab = 6일 때, a² + b² = ?",
          answer: "13",
          hint: "a² + b² = (a+b)² - 2ab",
          options: ["13", "19", "25", "11"]
        }
      ]
    },
    5: {
      name: "곱셈공식 변형 - 고급",
      difficulty: "어려움",
      reward: 200,
      questions: [
        {
          question: "a+b = 3, a²+b² = 5일 때, ab = ?",
          answer: "2",
          hint: "(a+b)² = a² + 2ab + b²",
          options: ["2", "4", "1", "3"]
        },
        {
          question: "(a+b+c)² - (a²+b²+c²) = ?",
          answer: "2(ab + bc + ca)",
          hint: "전개 후 정리",
          options: ["2(ab + bc + ca)", "ab + bc + ca", "3abc", "2abc"]
        },
        {
          question: "a - b = 4, ab = 5일 때, a² + b² = ?",
          answer: "26",
          hint: "a² + b² = (a-b)² + 2ab",
          options: ["26", "21", "16", "30"]
        },
        {
          question: "a+b = 6, a-b = 2일 때, ab = ?",
          answer: "8",
          hint: "두 식을 더하고 빼서 a, b 구하기",
          options: ["8", "12", "4", "10"]
        },
        {
          question: "x + 1/x = 3일 때, x² + 1/x² = ?",
          answer: "7",
          hint: "(x + 1/x)² = x² + 2 + 1/x²",
          options: ["7", "9", "11", "5"]
        }
      ]
    },
    6: {
      name: "최종 보스 테스트",
      difficulty: "매우 어려움",
      reward: 1000,
      isFinal: true,
      questions: [
        {
          question: "(a² + ab + b²)(a² - ab + b²) = ?",
          answer: "a⁴ + a²b² + b⁴",
          hint: "합차공식의 변형",
          options: ["a⁴ + a²b² + b⁴", "a⁴ - b⁴", "a⁴ + b⁴", "a²b²"]
        },
        {
          question: "a + b + c = 0일 때, a³ + b³ + c³ = ?",
          answer: "3abc",
          hint: "특수한 경우의 세제곱 관계",
          options: ["3abc", "0", "abc", "a² + b² + c²"]
        },
        {
          question: "x² + y² = 10, xy = 3일 때, (x+y)² = ?",
          answer: "16",
          hint: "(x+y)² = x² + 2xy + y²",
          options: ["16", "13", "19", "22"]
        },
        {
          question: "(x²+x+1)(x²-x+1) = ?",
          answer: "x⁴ + x² + 1",
          hint: "a=x², b=x로 치환",
          options: ["x⁴ + x² + 1", "x⁴ - 1", "x⁴ + 1", "x⁴ - x² + 1"]
        },
        {
          question: "a² + b² + c² = 30, ab + bc + ca = 25일 때, (a+b+c)² = ?",
          answer: "80",
          hint: "(a+b+c)² = a² + b² + c² + 2(ab+bc+ca)",
          options: ["80", "55", "60", "85"]
        },
        {
          question: "a⁴ + b⁴를 인수분해하면?",
          answer: "(a²+ab+b²)(a²-ab+b²)",
          hint: "a⁴ + b⁴ = (a²+b²)² - 2a²b²",
          options: [
            "(a²+ab+b²)(a²-ab+b²)",
            "(a²+b²)²",
            "(a+b)(a³+b³)",
            "인수분해 불가"
          ]
        },
        {
          question: "x + y = 5, x³ + y³ = 35일 때, xy = ?",
          answer: "6",
          hint: "x³ + y³ = (x+y)³ - 3xy(x+y)",
          options: ["6", "5", "8", "10"]
        },
        {
          question: "(a+b+c)³ - a³ - b³ - c³을 간단히 하면?",
          answer: "3(a+b)(b+c)(c+a)",
          hint: "고난도 전개 공식",
          options: [
            "3(a+b)(b+c)(c+a)",
            "3abc",
            "6abc",
            "(a+b+c)abc"
          ]
        },
        {
          question: "a² + b² = 1, a + b = √2일 때, ab = ?",
          answer: "1/2",
          hint: "(a+b)² = a² + 2ab + b²",
          options: ["1/2", "1", "√2/2", "0"]
        },
        {
          question: "a-b = 3, a³-b³ = 63일 때, ab = ?",
          answer: "6",
          hint: "a³-b³ = (a-b)³ + 3ab(a-b)",
          options: ["6", "9", "12", "3"]
        }
      ]
    }
  };

  useEffect(() => {
    if (isPlaying && gameMode === 'playing' && currentLevel === 6 && selected === null) {
      if (timeLeft > 0) {
        const timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000);
        return () => clearTimeout(timer);
      } else {
        handleWrongAnswer();
      }
    }
  }, [timeLeft, isPlaying, gameMode, currentLevel, selected]);

  const startLevel = (levelNum) => {
    if (!unlockedLevels.includes(levelNum)) return;
    
    setCurrentLevel(levelNum);
    setCurrentQuestion(0);
    setScore(0);
    setLives(3);
    setStreak(0);
    setSelected(null);
    setIsCorrect(null);
    setShowHint(false);
    setHintUsed(false);
    setTimeLeft(30);
    setIsPlaying(true);
    setGameMode('playing');
    setLevelStars(0);
  };

  const handleAnswer = (option) => {
    if (selected !== null) return;
    
    setSelected(option);
    const correct = option === levels[currentLevel].questions[currentQuestion].answer;
    setIsCorrect(correct);
    
    if (correct) {
      setScore(score + 1);
      setStreak(streak + 1);
      if (streak + 1 > maxStreak) setMaxStreak(streak + 1);
    } else {
      handleWrongAnswer();
    }
  };

  const handleWrongAnswer = () => {
    setStreak(0);
    const newLives = lives - 1;
    setLives(newLives);
    
    if (newLives <= 0) {
      setGameMode('gameOver');
      setIsPlaying(false);
    }
  };

  const nextQuestion = () => {
    const questionsLength = levels[currentLevel].questions.length;
    
    if (currentQuestion < questionsLength - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setSelected(null);
      setIsCorrect(null);
      setShowHint(false);
      setHintUsed(false);
      if (currentLevel === 6) setTimeLeft(30);
    } else {
      completeLevel();
    }
  };

  const completeLevel = () => {
    const questionsLength = levels[currentLevel].questions.length;
    const percentage = (score / questionsLength) * 100;
    
    let stars = 0;
    if (percentage === 100 && !hintUsed) stars = 3;
    else if (percentage === 100) stars = 2;
    else if (percentage >= 60) stars = 1;
    
    setLevelStars(stars);
    setTotalStars(totalStars + stars);
    
    const reward = levels[currentLevel].reward * (stars / 3);
    setTotalMoney(totalMoney + Math.floor(reward));
    
    if (stars > 0 && currentLevel < 6 && !unlockedLevels.includes(currentLevel + 1)) {
      setUnlockedLevels([...unlockedLevels, currentLevel + 1]);
    }
    
    setGameMode('levelComplete');
    setIsPlaying(false);
  };

  const goToMenu = () => {
    setGameMode('menu');
    setIsPlaying(false);
  };

  if (gameMode === 'menu') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 via-indigo-900 to-blue-900 p-4">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-8 pt-8">
            <div className="flex items-center justify-center gap-3 mb-4">
              <Trophy className="w-12 h-12 text-yellow-400" />
              <h1 className="text-5xl font-bold text-white">곱셈공식 마스터</h1>
              <Trophy className="w-12 h-12 text-yellow-400" />
            </div>
            <p className="text-xl text-purple-200">김민준 전용 학습 게임</p>
          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 mb-8">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <div className="text-center">
                <div className="flex items-center justify-center gap-2 mb-2">
                  <Star className="w-6 h-6 text-yellow-400" />
                  <span className="text-2xl font-bold text-white">{totalStars}</span>
                </div>
                <p className="text-purple-200 text-sm">총 별</p>
              </div>
              <div className="text-center">
                <div className="flex items-center justify-center gap-2 mb-2">
                  <Gift className="w-6 h-6 text-green-400" />
                  <span className="text-2xl font-bold text-white">{totalMoney}원</span>
                </div>
                <p className="text-purple-200 text-sm">획득 상금</p>
              </div>
              <div className="text-center">
                <div className="flex items-center justify-center gap-2 mb-2">
                  <Flame className="w-6 h-6 text-orange-400" />
                  <span className="text-2xl font-bold text-white">{maxStreak}</span>
                </div>
                <p className="text-purple-200 text-sm">최고 연속</p>
              </div>
              <div className="text-center">
                <div className="flex items-center justify-center gap-2 mb-2">
                  <Unlock className="w-6 h-6 text-blue-400" />
                  <span className="text-2xl font-bold text-white">{unlockedLevels.length}/6</span>
                </div>
                <p className="text-purple-200 text-sm">해금 레벨</p>
              </div>
            </div>
          </div>

          <div className="grid md:grid-cols-2 gap-6">
            {Object.entries(levels).map(([levelNum, level]) => {
              const isUnlocked = unlockedLevels.includes(parseInt(levelNum));
              const isFinal = level.isFinal;
              
              return (
                <div
                  key={levelNum}
                  className={`relative overflow-hidden rounded-2xl transition-all ${
                    isUnlocked
                      ? 'bg-gradient-to-br from-white/20 to-white/10 backdrop-blur-lg border-2 border-white/30 hover:scale-105 cursor-pointer'
                      : 'bg-gray-800/50 border-2 border-gray-700 cursor-not-allowed'
                  } ${isFinal ? 'md:col-span-2' : ''}`}
                  onClick={() => isUnlocked && startLevel(parseInt(levelNum))}
                >
                  {isFinal && (
                    <div className="absolute inset-0 bg-gradient-to-r from-yellow-500/20 to-red-500/20 animate-pulse" />
                  )}
                  
                  <div className="relative p-6">
                    <div className="flex items-start justify-between mb-4">
                      <div>
                        <div className="flex items-center gap-2 mb-2">
                          {isUnlocked ? (
                            <Unlock className="w-6 h-6 text-green-400" />
                          ) : (
                            <Lock className="w-6 h-6 text-gray-500" />
                          )}
                          <h3 className={`text-2xl font-bold ${isUnlocked ? 'text-white' : 'text-gray-500'}`}>
                            레벨 {levelNum}
                          </h3>
                        </div>
                        <p className={`text-xl mb-2 ${isUnlocked ? 'text-white' : 'text-gray-500'}`}>
                          {level.name}
                        </p>
                        <div className="flex items-center gap-4">
                          <span className={`px-3 py-1 rounded-full text-sm font-bold ${
                            level.difficulty === '쉬움' ? 'bg-green-500/20 text-green-300' :
                            level.difficulty === '보통' ? 'bg-yellow-500/20 text-yellow-300' :
                            level.difficulty === '어려움' ? 'bg-orange-500/20 text-orange-300' :
                            'bg-red-500/20 text-red-300'
                          }`}>
                            {level.difficulty}
                          </span>
                          <div className="flex items-center gap-1">
                            <Gift className="w-4 h-4 text-yellow-400" />
                            <span className="text-yellow-400 font-bold">{level.reward}원</span>
                          </div>
                        </div>
                      </div>
                      
                      {isFinal && (
                        <Trophy className="w-16 h-16 text-yellow-400 animate-bounce" />
                      )}
                    </div>
                    
                    <div className="text-sm text-purple-200">
                      문제 {level.questions.length}개
                    </div>
                    
                    {!isUnlocked && (
                      <div className="absolute inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center">
                        <div className="text-center">
                          <Lock className="w-12 h-12 text-gray-400 mx-auto mb-2" />
                          <p className="text-gray-300 font-bold">이전 레벨을 클리어하세요!</p>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    );
  }

  if (gameMode === 'gameOver') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-red-900 via-red-800 to-orange-900 p-4 flex items-center justify-center">
        <div className="max-w-2xl w-full bg-white rounded-2xl shadow-2xl p-8 text-center">
          <XCircle className="w-24 h-24 mx-auto mb-6 text-red-500" />
          <h2 className="text-4xl font-bold text-gray-800 mb-4">게임 오버!</h2>
          <p className="text-xl text-gray-600 mb-4">생명이 모두 소진되었습니다.</p>
          <div className="text-3xl font-bold text-indigo-600 mb-8">
            획득 점수: {score} / {levels[currentLevel].questions.length}
          </div>
          <div className="flex gap-4 justify-center">
            <button
              onClick={() => startLevel(currentLevel)}
              className="bg-indigo-600 text-white px-6 py-3 rounded-xl font-bold hover:bg-indigo-700 transition flex items-center gap-2"
            >
              <RefreshCw className="w-5 h-5" />
              다시 도전
            </button>
            <button
              onClick={goToMenu}
              className="bg-gray-600 text-white px-6 py-3 rounded-xl font-bold hover:bg-gray-700 transition"
            >
              메뉴로
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (gameMode === 'levelComplete') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-green-900 via-emerald-800 to-teal-900 p-4 flex items-center justify-center">
        <div className="max-w-2xl w-full bg-white rounded-2xl shadow-2xl p-8 text-center">
          <Trophy className="w-24 h-24 mx-auto mb-6 text-yellow-500" />
          <h2 className="text-4xl font-bold text-gray-800 mb-4">레벨 클리어! 🎉</h2>
          
          <div className="flex justify-center gap-2 mb-6">
            {[1, 2, 3].map((star) => (
              <Star
                key={star}
                className={`w-12 h-12 ${star <= levelStars ? 'text-yellow-500 fill-yellow-500' : 'text-gray-300'}`}
              />
            ))}
          </div>

          <div className="mb-6">
            <div className="text-3xl font-bold text-indigo-600 mb-2">
              {score} / {levels[currentLevel].questions.length}
            </div>
            <p className="text-gray-600">정답률: {Math.round((score / levels[currentLevel].questions.length) * 100)}%</p>
          </div>

          <div className="bg-green-50 border-2 border-green-500 rounded-xl p-4 mb-6">
            <div className="flex items-center justify-center gap-2 mb-2">
              <Gift className="w-6 h-6 text-green-600" />
              <span className="text-2xl font-bold text-green-600">
                +{Math.floor(levels[currentLevel].reward * (levelStars / 3))}원
              </span>
            </div>
            <p className="text-sm text-gray-600">총 상금: {totalMoney}원</p>
          </div>

          {levelStars === 3 && (
            <p className="text-green-600 text-xl font-bold mb-4">🏆 완벽해요! 별 3개 획득!</p>
          )}
          {levelStars === 2 && (
            <p className="text-blue-600 text-xl font-bold mb-4">👏 훌륭해요! 별 2개!</p>
          )}
          {levelStars === 1 && (
            <p className="text-yellow-600 text-xl font-bold mb-4">💪 좋아요! 별 1개!</p>
          )}

          <div className="flex gap-4 justify-center">
            <button
              onClick={() => startLevel(currentLevel)}
              className="bg-indigo-600 text-white px-6 py-3 rounded-xl font-bold hover:bg-indigo-700 transition flex items-center gap-2"
            >
              <RefreshCw className="w-5 h-5" />
              다시 도전
            </button>
            {currentLevel < 6 && unlockedLevels.includes(currentLevel + 1) && (
              <button
                onClick={() => startLevel(currentLevel + 1)}
                className="bg-green-600 text-white px-6 py-3 rounded-xl font-bold hover:bg-green-700 transition flex items-center gap-2"
              >
                다음 레벨
                <TrendingUp className="w-5 h-5" />
              </button>
            )}
            <button
              onClick={goToMenu}
              className="bg-gray-600 text-white px-6 py-3 rounded-xl font-bold hover:bg-gray-700 transition"
            >
              메뉴로
            </button>
          </div>
        </div>
      </div>
    );
  }

  const currentQ = levels[currentLevel].questions[currentQuestion];

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 p-4">
      <div className="max-w-4xl mx-auto pt-8">
        {/* 상단 정보 바 */}
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-4 mb-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-4">
              <div className="flex items-center gap-2">
                <Heart className="w-6 h-6 text-red-400" />
                {[...Array(3)].map((_, i) => (
                  <Heart
                    key={i}
                    className={`w-6 h-6 ${i < lives ? 'text-red-500 fill-red-500' : 'text-gray-500'}`}
                  />
                ))}
              </div>
              <div className="flex items-center gap-2">
                <Flame className="w-6 h-6 text-orange-400" />
                <span className="text-white font-bold text-xl">{streak}</span>
              </div>
            </div>
            
            {currentLevel === 6 && (
              <div className="flex items-center gap-2">
                <Clock className="w-6 h-6 text-yellow-400" />
                <span className={`text-2xl font-bold ${timeLeft <= 10 ? 'text-red-400 animate-pulse' : 'text-white'}`}>
                  {timeLeft}초
                </span>
              </div>
            )}

            <div className="text-right">
              <div className="text-white text-sm mb-1">레벨 {currentLevel}</div>
              <div className="text-white font-bold">
                {currentQuestion + 1} / {levels[currentLevel].questions.length}
              </div>
            </div>
          </div>

          {/* 진행 바 */}
          <div className="w-full bg-white/20 rounded-full h-3 overflow-hidden">
            <div
              className="bg-gradient-to-r from-green-400 to-blue-500 h-full transition-all duration-300"
              style={{ width: `${((currentQuestion + 1) / levels[currentLevel].questions.length) * 100}%` }}
            />
          </div>
        </div>

        {/* 문제 카드 */}
        <div className="bg-white rounded-2xl shadow-2xl p-8 mb-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800">{levels[currentLevel].name}</h2>
            <div className="flex items-center gap-2">
              <Target className="w-6 h-6 text-indigo-600" />
              <span className="text-xl font-bold text-indigo-600">{score}점</span>
            </div>
          </div>

          <div className="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-xl p-6 mb-6">
            <p className="text-4xl font-bold text-center text-gray-800 mb-4">
              {currentQ.question}
            </p>
          </div>

          {/* 힌트 버튼 */}
          {!showHint && selected === null && (
            <button
              onClick={() => {
                setShowHint(true);
                setHintUsed(true);
              }}
              className="w-full mb-4 bg-yellow-500 text-white py-3 rounded-xl font-bold hover:bg-yellow-600 transition flex items-center justify-center gap-2"
            >
              <Brain className="w-5 h-5" />
              힌트 보기 (별 감소)
            </button>
          )}

          {/* 힌트 표시 */}
          {showHint && (
            <div className="bg-yellow-50 border-2 border-yellow-400 rounded-xl p-4 mb-6">
              <div className="flex items-start gap-2">
                <Zap className="w-5 h-5 text-yellow-600 mt-1 flex-shrink-0" />
                <div>
                  <p className="font-bold text-yellow-800 mb-1">💡 힌트</p>
                  <p className="text-yellow-700">{currentQ.hint}</p>
                </div>
              </div>
            </div>
          )}

          {/* 선택지 */}
          <div className="space-y-3">
            {currentQ.options.map((option, index) => {
              let buttonClass = "w-full p-4 rounded-xl font-bold text-lg transition-all transform hover:scale-102 ";
              
              if (selected === null) {
                buttonClass += "bg-gradient-to-r from-indigo-500 to-purple-500 text-white hover:from-indigo-600 hover:to-purple-600";
              } else if (option === currentQ.answer) {
                buttonClass += "bg-green-500 text-white ring-4 ring-green-300";
              } else if (option === selected && !isCorrect) {
                buttonClass += "bg-red-500 text-white ring-4 ring-red-300";
              } else {
                buttonClass += "bg-gray-300 text-gray-600";
              }

              return (
                <button
                  key={index}
                  onClick={() => handleAnswer(option)}
                  disabled={selected !== null}
                  className={buttonClass}
                >
                  <div className="flex items-center justify-between">
                    <span>{option}</span>
                    {selected !== null && option === currentQ.answer && (
                      <CheckCircle className="w-6 h-6" />
                    )}
                    {selected === option && !isCorrect && (
                      <XCircle className="w-6 h-6" />
                    )}
                  </div>
                </button>
              );
            })}
          </div>

          {/* 다음 문제 버튼 */}
          {selected !== null && (
            <div className="mt-6">
              {isCorrect && (
                <div className="bg-green-50 border-2 border-green-500 rounded-xl p-4 mb-4">
                  <div className="flex items-center gap-2">
                    <CheckCircle className="w-6 h-6 text-green-600" />
                    <p className="text-green-800 font-bold text-lg">정답입니다! 🎉</p>
                  </div>
                  {streak > 0 && (
                    <p className="text-green-600 text-sm mt-2">🔥 {streak}연속 정답!</p>
                  )}
                </div>
              )}
              {!isCorrect && (
                <div className="bg-red-50 border-2 border-red-500 rounded-xl p-4 mb-4">
                  <div className="flex items-center gap-2">
                    <XCircle className="w-6 h-6 text-red-600" />
                    <p className="text-red-800 font-bold text-lg">틀렸습니다 💪</p>
                  </div>
                  <p className="text-red-600 text-sm mt-2">정답: {currentQ.answer}</p>
                </div>
              )}
              
              <button
                onClick={nextQuestion}
                className="w-full bg-gradient-to-r from-blue-500 to-indigo-600 text-white py-4 rounded-xl font-bold text-xl hover:from-blue-600 hover:to-indigo-700 transition flex items-center justify-center gap-2"
              >
                {currentQuestion < levels[currentLevel].questions.length - 1 ? (
                  <>다음 문제 <TrendingUp className="w-6 h-6" /></>
                ) : (
                  <>결과 보기 <Award className="w-6 h-6" /></>
                )}
              </button>
            </div>
          )}
        </div>

        {/* 하단 버튼 */}
        <div className="flex justify-center">
          <button
            onClick={goToMenu}
            className="bg-white/20 backdrop-blur-lg text-white px-6 py-3 rounded-xl font-bold hover:bg-white/30 transition"
          >
            메뉴로 돌아가기
          </button>
        </div>
      </div>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<MultiplicationMasterGame />);

    </script>
</body>
</html>
"""

st.set_page_config(page_title="곱셈공식 마스터", layout="wide")
components.html(html_code, height=1000, scrolling=True)
