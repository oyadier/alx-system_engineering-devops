# declarative scrip for installing packeg using
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
/* puppet declarative script to grab puppet-lint
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}*/
