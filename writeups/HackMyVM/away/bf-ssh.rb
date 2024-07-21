require 'open3'

if ARGV.size == 2
  password_found = false

  File.readlines(ARGV[1], chomp: true).each do |password|
    Open3.popen3("ssh-keygen -y -f #{ARGV[0]} -P '#{password}'") { |i,o,e,t|
      error = e.read.chomp
      if error.empty?
        puts "\nThe password is: #{password}"
        password_found = true
      elsif /incorrect passphrase supplied to decrypt private key/.match?(error)
        print '.'
      else
        puts "Error: #{t.value}"
        puts error
      end
    }
    break if password_found
  end
else
  puts "Usage  : ruby #{__FILE__} SSH_KEY WORDLIST"
  puts "Example: ruby #{__FILE__} ~/.ssh/id_ed25519_crack /usr/share/wordlists/passwords/richelieu-french-top20000.txt"
end
