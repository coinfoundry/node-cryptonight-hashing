{
    "targets": [
        {
            "target_name": "cryptonight-hashing",
            "sources": [
                "multihashing.cc",
                "xmrig/crypto/c_blake256.c",
                "xmrig/crypto/c_groestl.c",
                "xmrig/crypto/c_jh.c",
                "xmrig/crypto/c_keccak.c",
                "xmrig/crypto/c_skein.c"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_c": [
                "-std=gnu11", "-march=native", "-fPIC", "-m64", "-DNDEBUG", "-Ofast", "-funroll-loops", "-fvariable-expansion-in-unroller", "-ftree-loop-if-convert-stores", "-fmerge-all-constants", "-fbranch-target-load-optimize2"
            ],
            "cflags_cc": [
                "-std=gnu++11", "-march=native", "-fPIC", "-m64", "-DNDEBUG", "-Ofast", "-s", "-funroll-loops", "-fvariable-expansion-in-unroller", "-ftree-loop-if-convert-stores", "-fmerge-all-constants", "-fbranch-target-load-optimize2"
            ],
            "conditions": [
                ['OS=="openbsd" or OS=="freebsd"', {
                    "cflags_c!": [ "-fvariable-expansion-in-unroller", "-ftree-loop-if-convert-stores", "-fmerge-all-constants", "-fbranch-target-load-optimize2" ],
                    "cflags_cc!": [ "-fvariable-expansion-in-unroller", "-ftree-loop-if-convert-stores", "-fmerge-all-constants", "-fbranch-target-load-optimize2" ],
                    "cflags": [
                        "-O2",
                        "-Wno-unused-function",
                        "-Wno-unused-variable",
                        "-Wno-missing-braces",
                        "-Wno-unused-private-field",
                        "-Wno-deprecated-declarations"
                    ],
                    'include_dirs': [
                        '/usr/local/include'],
                    'libraries': [
                        '-L/usr/local/lib']
                }],
            ]
        }
    ]
}
