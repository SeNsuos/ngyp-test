{
    "targets": [
        {
          "target_name": "addon",
          "cflags!": [ "-fno-exceptions" ],
          "cflags_cc!": [ "-fno-exceptions" ],
          "sources": [ "src/cpp/addon.cpp" ],
          "include_dirs": [
            "<!@(node -p \"require('node-addon-api').include\")"
          ],
          "dependencies": [
            "<!(node -p \"require('node-addon-api').gyp\")"
          ],
          'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],

          'msvs_settings': {
              'VCCLCompilerTool': {
                'ExceptionHandling': '1',
                'AdditionalOptions': ['/EHsc']
              }
          }

        }
   ]
}