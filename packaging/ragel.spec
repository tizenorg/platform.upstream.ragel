Name:       ragel
Summary:    Ragel State Machine Compiler
Version:    6.6
Release:    1
Group:      System/Utilities
License:    GPL-2.0
Source0:    %{name}-%{version}.tar.gz

%description
compiles finite state machines into code in various languages
Ragel compiles finite state machines from regular languages into C, C++,
Objective-C, D, Ruby or Java code. Ragel allows the programmer to embed
actions at any point in a regular language. Non-determinism can be
controlled through the use of embedded priorities and guarded regular
language operators. Ragel also supports the construction of scanners and
the building of state machines using state-charts. Ragel can be used to
create robust recognizers and parsers which run very fast. It can work
with integer-sized alphabets and can compile large state machines.
The generated code has no dependencies.


%prep
%setup -q 

%build
%autogen.sh
%configure --prefix=%{_prefix}

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install

%remove_docs

%files
%license COPYING
%manifest ragel.manifest
%{_bindir}/ragel
