"""
Code Evaluator for Coding Challenges
Evaluates submitted code against test cases
"""

import subprocess
import json
import tempfile
import os
from typing import Dict, List, Any, Tuple


class CodeExecutionResult:
    """Result of code execution."""

    def __init__(self):
        self.success = False
        self.passed_tests = 0
        self.total_tests = 0
        self.output = ""
        self.error = ""
        self.time_taken = 0.0
        self.test_results = []

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            'success': self.success,
            'passed_tests': self.passed_tests,
            'total_tests': self.total_tests,
            'output': self.output,
            'error': self.error,
            'time_taken': self.time_taken,
            'test_results': self.test_results,
            'score': (self.passed_tests / self.total_tests * 100) if self.total_tests > 0 else 0
        }


class CodeEvaluator:
    """Evaluates coding challenge submissions."""

    def __init__(self):
        self.timeout = 5  # seconds per execution
        self.max_output_length = 10000

    def evaluate_java(self, code: str, test_cases: List[Dict]) -> CodeExecutionResult:
        """Evaluate Java code."""
        result = CodeExecutionResult()

        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.java', delete=False) as f:
                f.write(code)
                temp_file = f.name

            # Extract class name and compile
            try:
                subprocess.run(['javac', temp_file], check=True, capture_output=True, timeout=self.timeout)
            except subprocess.CalledProcessError as e:
                result.error = f"Compilation error: {e.stderr.decode()}"
                return result
            except FileNotFoundError:
                result.error = "Java compiler not found. Please ensure Java is installed."
                return result

            # Run tests
            result.total_tests = len(test_cases)
            class_name = temp_file.replace('.java', '').split('/')[-1]

            for i, test_case in enumerate(test_cases):
                try:
                    # Execute the compiled code
                    exec_result = subprocess.run(
                        ['java', '-cp', os.path.dirname(temp_file), class_name],
                        input=test_case.get('input', ''),
                        capture_output=True,
                        text=True,
                        timeout=self.timeout
                    )

                    output = exec_result.stdout.strip()
                    expected = test_case.get('expected_output', '').strip()

                    test_passed = output == expected
                    if test_passed:
                        result.passed_tests += 1

                    result.test_results.append({
                        'test_number': i + 1,
                        'passed': test_passed,
                        'input': test_case.get('input', 'N/A'),
                        'expected': expected,
                        'actual': output if not exec_result.returncode else f"Error: {exec_result.stderr}"
                    })

                except subprocess.TimeoutExpired:
                    result.test_results.append({
                        'test_number': i + 1,
                        'passed': False,
                        'error': 'Execution timed out'
                    })

            result.success = result.passed_tests == result.total_tests

        except Exception as e:
            result.error = str(e)

        finally:
            # Cleanup
            try:
                if 'temp_file' in locals():
                    os.remove(temp_file)
                    class_file = temp_file.replace('.java', '.class')
                    if os.path.exists(class_file):
                        os.remove(class_file)
            except:
                pass

        return result

    def evaluate_python(self, code: str, test_cases: List[Dict]) -> CodeExecutionResult:
        """Evaluate Python code."""
        result = CodeExecutionResult()

        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name

            result.total_tests = len(test_cases)

            for i, test_case in enumerate(test_cases):
                try:
                    # Execute Python code
                    exec_result = subprocess.run(
                        ['python', temp_file],
                        input=test_case.get('input', ''),
                        capture_output=True,
                        text=True,
                        timeout=self.timeout
                    )

                    output = exec_result.stdout.strip()
                    expected = test_case.get('expected_output', '').strip()

                    test_passed = output == expected
                    if test_passed:
                        result.passed_tests += 1

                    result.test_results.append({
                        'test_number': i + 1,
                        'passed': test_passed,
                        'input': test_case.get('input', 'N/A'),
                        'expected': expected,
                        'actual': output if not exec_result.returncode else f"Error: {exec_result.stderr}"
                    })

                except subprocess.TimeoutExpired:
                    result.test_results.append({
                        'test_number': i + 1,
                        'passed': False,
                        'error': 'Execution timed out'
                    })

            result.success = result.passed_tests == result.total_tests

        except Exception as e:
            result.error = str(e)

        finally:
            try:
                if 'temp_file' in locals():
                    os.remove(temp_file)
            except:
                pass

        return result

    def evaluate_javascript(self, code: str, test_cases: List[Dict]) -> CodeExecutionResult:
        """Evaluate JavaScript code."""
        result = CodeExecutionResult()

        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
                f.write(code)
                temp_file = f.name

            result.total_tests = len(test_cases)

            for i, test_case in enumerate(test_cases):
                try:
                    exec_result = subprocess.run(
                        ['node', temp_file],
                        input=test_case.get('input', ''),
                        capture_output=True,
                        text=True,
                        timeout=self.timeout
                    )

                    output = exec_result.stdout.strip()
                    expected = test_case.get('expected_output', '').strip()

                    test_passed = output == expected
                    if test_passed:
                        result.passed_tests += 1

                    result.test_results.append({
                        'test_number': i + 1,
                        'passed': test_passed,
                        'input': test_case.get('input', 'N/A'),
                        'expected': expected,
                        'actual': output if not exec_result.returncode else f"Error: {exec_result.stderr}"
                    })

                except subprocess.TimeoutExpired:
                    result.test_results.append({
                        'test_number': i + 1,
                        'passed': False,
                        'error': 'Execution timed out'
                    })

            result.success = result.passed_tests == result.total_tests

        except Exception as e:
            result.error = str(e)

        finally:
            try:
                if 'temp_file' in locals():
                    os.remove(temp_file)
            except:
                pass

        return result

    def evaluate_code(self, code: str, language: str, test_cases: List[Dict]) -> CodeExecutionResult:
        """Evaluate code in any supported language."""
        language = language.lower()

        if language == 'java':
            return self.evaluate_java(code, test_cases)
        elif language == 'python':
            return self.evaluate_python(code, test_cases)
        elif language == 'javascript':
            return self.evaluate_javascript(code, test_cases)
        else:
            result = CodeExecutionResult()
            result.error = f"Language {language} not supported for evaluation"
            return result

    def evaluate_code_quality(self, code: str, language: str) -> Dict[str, Any]:
        """Evaluate code quality metrics."""
        metrics = {
            'lines_of_code': len(code.strip().split('\n')),
            'has_comments': '#' in code or '//' in code or '/*' in code,
            'complexity_estimate': self._estimate_complexity(code),
            'style_issues': []
        }

        # Basic style checks
        lines = code.split('\n')
        for i, line in enumerate(lines):
            if len(line) > 120:
                metrics['style_issues'].append(f"Line {i+1}: Too long ({len(line)} chars)")

        return metrics

    def _estimate_complexity(self, code: str) -> str:
        """Estimate time complexity from code patterns."""
        # Simple heuristic-based complexity estimation
        nested_loops = 0
        if 'for' in code or 'while' in code:
            for line in code.split('\n'):
                if 'for' in line or 'while' in line:
                    # Count indentation level
                    indent = len(line) - len(line.lstrip())
                    nested_loops = max(nested_loops, indent // 4)

        if nested_loops >= 3:
            return "O(n^3) or worse - potential performance issue"
        elif nested_loops == 2:
            return "O(n^2) - may be inefficient for large inputs"
        elif nested_loops == 1:
            return "O(n) - likely acceptable"
        else:
            return "O(1) or O(log n) - likely optimal"


# Singleton instance
_evaluator = None


def get_code_evaluator() -> CodeEvaluator:
    """Get or create code evaluator instance."""
    global _evaluator
    if _evaluator is None:
        _evaluator = CodeEvaluator()
    return _evaluator
