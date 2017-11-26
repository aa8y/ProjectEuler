package co.aa8y.euler

import org.scalatest.FunSpec

class Problem0001Spec extends FunSpec {
  describe("Problem 1: Multiples of 3 and 5.") {
    describe("Sum of natural numbers which are multiples of 3 and 5 below") {
      it("10 should be 23.") {
        val expected = 23
        val computed = Problem0001.solution(1 until 10)

        assert(computed === expected)
      }
      it("1000 should be 233168.") {
        val expected = 233168
        val computed = Problem0001.solution(1 until 1000)

        assert(computed === expected)
      }
    }
  }
}
