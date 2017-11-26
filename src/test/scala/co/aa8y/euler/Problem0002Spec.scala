package co.aa8y.euler

import org.scalatest.FunSpec

class Problem0002Spec extends FunSpec {
  describe("Problem 2: Even Fibonacci numbers.") {
    describe("Sum of even Fibonacci numbers below") {
      it("10 should be 10.") {
        val expected = 10
        val computed = Problem0002.solution(10)

        assert(computed === expected)
      }
      it("100 should be 233168.") {
        val expected = 44
        val computed = Problem0002.solution(100)

        assert(computed === expected)
      }
    }
  }
}
