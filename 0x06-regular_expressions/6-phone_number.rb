#!/usr/bin/env ruby
# Match exactly ten digit number
puts ARGV[0].scan(/[0-9]{10}/).join
