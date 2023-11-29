#!/usr/bin/env ruby
# Match exactly ten digit number
puts ARGV[0].scan(/^\d[10]$/).join
