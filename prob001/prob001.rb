#!/usr/bin/env ruby
require 'benchmark'

puts Benchmark.measure {
  sum = 0
  for i in (1...1000)
    if i % 3 == 0 or i % 5 == 0
      sum = sum + i
      #puts i
    end
  end
  puts sum
}

puts Benchmark.measure {
  sum = 0
  (3...1000).step(3).each { |i| sum += i }
  (5...1000).step(5).each { |i| sum += i }
  (15...1000).step(15).each { |i| sum -= i }
  puts sum
}

# Based on explanation pdf
# n = divisible by
# target = top of range
def SumDivisibleBy(n, target = 999)
  p = target / n
  return n*(p*(p+1)) / 2
end

puts Benchmark.measure {
  puts SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15)
}
