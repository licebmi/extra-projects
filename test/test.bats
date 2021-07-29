@test "Run without arguments" {
  run ./number-printer.py
  [ "$status" -eq 0 ]
  [ "$(echo \"$output\" | egrep -v '[0-9]')" = "" ]
}

@test "Run with ordered output" {
  run ./number-printer.py -o
  [ "$status" -eq 0 ]
  [ "$output" = "$(printf '1\n2\n3\n4\n5\n6\n7\n8\n9\n10')" ]
}


@test "Run with offset" {
  run ./number-printer.py -o -s 2
  [ "$status" -eq 0 ]
  [ "$output" = "$(printf '2\n3\n4\n5\n6\n7\n8\n9\n10\n11')" ]
}



@test "Run with extra numbers" {
  run ./number-printer.py -o 12
  [ "$status" -eq 0 ]
  [ "$output" = "$(printf '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12')" ]
}
