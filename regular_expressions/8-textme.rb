#!/usr/bin/env ruby

# Extract the sender, receiver, and flags using a regular expression
log = ARGV[0]
matches = log.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# Ensure there is a match, and output the required format
if matches.any?
  sender, receiver, flags = matches[0]
  puts "#{sender},#{receiver},#{flags}"
end
