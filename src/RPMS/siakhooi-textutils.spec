Name:           siakhooi-textutils
Version:        1.10.1
Release:        1%{?dist}
Summary:        commands to transform line of texts.

License:        MIT
URL:            https://github.com/siakhooi/textutils
Source0:        https://github.com/siakhooi/%{name}/archive/refs/tags/${version}.tar.gz
BuildArch:      noarch

Requires:       bash

%description
commands to transform line of texts.

%install
%{__mkdir}   -v -p %{buildroot}%{_bindir}
%{__mkdir}   -v -p %{buildroot}%{_mandir}/man1
%{__mkdir}   -v -p %{buildroot}/usr/share/licenses/siakhooi-textutils
%{__install} -v -m 0755 %{_topdir}/BUILD/usr/bin/* %{buildroot}%{_bindir}
%{__install} -v -m 644  %{_topdir}/BUILD/usr/share/man/man1/* %{buildroot}%{_mandir}/man1
%{__install} -v -m 644  %{_topdir}/BUILD/LICENSE %{buildroot}/usr/share/licenses/siakhooi-textutils

%files
%license LICENSE
%{_bindir}/is-false
%{_bindir}/is-true
%{_bindir}/make-table
%{_bindir}/hyperlink
%{_bindir}/prefix
%{_bindir}/suffix
%{_bindir}/nvl
%{_mandir}/man1/is-false.1.gz
%{_mandir}/man1/is-true.1.gz
%{_mandir}/man1/make-table.1.gz
%{_mandir}/man1/prefix.1.gz
%{_mandir}/man1/siakhooi-textutils.1.gz
%{_mandir}/man1/suffix.1.gz

%changelog
* Mon May 25 2026 Siak Hooi <siakhooi@gmail.com> - 1.10.1
- fix make-table bug

* Wed May 20 2026 Siak Hooi <siakhooi@gmail.com> - 1.10.0
- hardening

* Sun Dec 28 2025 Siak Hooi <siakhooi@gmail.com> - 1.9.0
- add hyperlink

* Sat Nov 9 2024 Siak Hooi <siakhooi@gmail.com> - 1.8.0
- add nvl

* Mon Nov 4 2024 Siak Hooi <siakhooi@gmail.com> - 1.7.5
- fix man page

* Mon Nov 4 2024 Siak Hooi <siakhooi@gmail.com> - 1.7.4
- initial rpm version

* Tue Oct 29 2024 Siak Hooi <siakhooi@gmail.com> - 1.7.3
- fix workflow dependency

* Tue Oct 29 2024 Siak Hooi <siakhooi@gmail.com> - 1.7.2
- refactor deb workflow

* Tue Oct 29 2024 Siak Hooi <siakhooi@gmail.com> - 1.7.1
- add release automation

* Sun Dec 10 2023 Siak Hooi <siakhooi@gmail.com> - 1.7.0
- add make-table

* Fri May 19 2023 Siak Hooi <siakhooi@gmail.com> - 1.6.2
- fix file owner and permission

* Thu Apr 20 2023 Siak Hooi <siakhooi@gmail.com> - 1.6.1
- bug fixes

* Sun Apr 16 2023 Siak Hooi <siakhooi@gmail.com> - 1.6.0
- prefix/suffix: add inputFile parameter

* Sun Apr 16 2023 Siak Hooi <siakhooi@gmail.com> - 1.5.1
- fix wf issue

* Sun Apr 16 2023 Siak Hooi <siakhooi@gmail.com> - 1.5.0
- replace with bash string substitutions

* Tue Mar 28 2023 Siak Hooi <siakhooi@gmail.com> - 1.4.0
- remove indent, update doc

* Fri Mar 24 2023 Siak Hooi <siakhooi@gmail.com> - 1.3.0
- add is-true, is-false

* Mon Mar 20 2023 Siak Hooi <siakhooi@gmail.com> - 1.2.0
- add prefix, suffix

* Mon Mar 20 2023 Siak Hooi <siakhooi@gmail.com> - 1.1.0
- rename to textutils

* Sun Mar 19 2023 Siak Hooi <siakhooi@gmail.com> - 1.0.2
- fix md, deb compression

* Fri Mar 03 2023 Siak Hooi <siakhooi@gmail.com> - 1.0.1
- fix man page

* Fri Mar 03 2023 Siak Hooi <siakhooi@gmail.com> - 1.0.0
- initial version
