#this fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-apache-500-error':
  command => '/path/to/fix/script/or/command',
  onlyif  => '/path/to/check/if/fix/is/needed',
}
