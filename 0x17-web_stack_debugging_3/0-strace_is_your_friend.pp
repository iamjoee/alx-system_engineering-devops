#this fixes why Apache is returning a 500 error.`.

exec { 'fix-apache-500-error':
  command => '/path/to/fix/script/or/command',
  onlyif  => '/path/to/check/if/fix/is/needed',
}
