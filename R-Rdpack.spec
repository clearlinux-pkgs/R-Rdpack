#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Rdpack
Version  : 2.3
Release  : 42
URL      : https://cran.r-project.org/src/contrib/Rdpack_2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rdpack_2.3.tar.gz
Summary  : Update and Manipulate Rd Documentation Objects
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-rbibutils
BuildRequires : R-rbibutils
BuildRequires : buildreq-R

%description
including functions reprompt() and ereprompt() for updating 'Rd'
    documentation for functions, methods and classes; 'Rd' macros for
    citations and import of references from 'bibtex' files for use in
    'Rd' files and 'roxygen2' comments; 'Rd' macros for evaluating and
    inserting snippets of 'R' code and the results of its evaluation or
    creating graphics on the fly; and many functions for manipulation of
    references and Rd files.

%prep
%setup -q -c -n Rdpack
cd %{_builddir}/Rdpack

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648152349

%install
export SOURCE_DATE_EPOCH=1648152349
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rdpack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rdpack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rdpack
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Rdpack || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Rdpack/CITATION
/usr/lib64/R/library/Rdpack/DESCRIPTION
/usr/lib64/R/library/Rdpack/INDEX
/usr/lib64/R/library/Rdpack/Meta/Rd.rds
/usr/lib64/R/library/Rdpack/Meta/features.rds
/usr/lib64/R/library/Rdpack/Meta/hsearch.rds
/usr/lib64/R/library/Rdpack/Meta/links.rds
/usr/lib64/R/library/Rdpack/Meta/nsInfo.rds
/usr/lib64/R/library/Rdpack/Meta/package.rds
/usr/lib64/R/library/Rdpack/Meta/vignette.rds
/usr/lib64/R/library/Rdpack/NAMESPACE
/usr/lib64/R/library/Rdpack/NEWS.md
/usr/lib64/R/library/Rdpack/R/Rdpack
/usr/lib64/R/library/Rdpack/R/Rdpack.rdb
/usr/lib64/R/library/Rdpack/R/Rdpack.rdx
/usr/lib64/R/library/Rdpack/REFERENCES.bib
/usr/lib64/R/library/Rdpack/RStudio/addins.dcf
/usr/lib64/R/library/Rdpack/auto/REFERENCES.el
/usr/lib64/R/library/Rdpack/doc/Inserting_bibtex_references.R
/usr/lib64/R/library/Rdpack/doc/Inserting_bibtex_references.Rnw
/usr/lib64/R/library/Rdpack/doc/Inserting_bibtex_references.pdf
/usr/lib64/R/library/Rdpack/doc/Inserting_figures_and_evaluated_examples.R
/usr/lib64/R/library/Rdpack/doc/Inserting_figures_and_evaluated_examples.Rnw
/usr/lib64/R/library/Rdpack/doc/Inserting_figures_and_evaluated_examples.pdf
/usr/lib64/R/library/Rdpack/doc/index.html
/usr/lib64/R/library/Rdpack/examples/Rdpack-package.Rd
/usr/lib64/R/library/Rdpack/examples/RdpackTester.pdf
/usr/lib64/R/library/Rdpack/examples/RdpackTester/DESCRIPTION
/usr/lib64/R/library/Rdpack/examples/RdpackTester/NAMESPACE
/usr/lib64/R/library/Rdpack/examples/RdpackTester/R/RdpackTester-internal.R
/usr/lib64/R/library/Rdpack/examples/RdpackTester/inst/REFERENCES.bib
/usr/lib64/R/library/Rdpack/examples/RdpackTester/inst/auto/REFERENCES.el
/usr/lib64/R/library/Rdpack/examples/RdpackTester/man/RdpackTester-package.Rd
/usr/lib64/R/library/Rdpack/examples/journal_with_percents.bib
/usr/lib64/R/library/Rdpack/examples/reprompt.Rd
/usr/lib64/R/library/Rdpack/examples/tz.Rd
/usr/lib64/R/library/Rdpack/examples/url_with_percents.bib
/usr/lib64/R/library/Rdpack/help/AnIndex
/usr/lib64/R/library/Rdpack/help/Rdpack.rdb
/usr/lib64/R/library/Rdpack/help/Rdpack.rdx
/usr/lib64/R/library/Rdpack/help/aliases.rds
/usr/lib64/R/library/Rdpack/help/macros/refmacros.Rd
/usr/lib64/R/library/Rdpack/help/paths.rds
/usr/lib64/R/library/Rdpack/html/00Index.html
/usr/lib64/R/library/Rdpack/html/R.css
/usr/lib64/R/library/Rdpack/tests/testthat.R
/usr/lib64/R/library/Rdpack/tests/testthat/StructureClasses.Rd
/usr/lib64/R/library/Rdpack/tests/testthat/as.character.f_usage.Rd
/usr/lib64/R/library/Rdpack/tests/testthat/char2Rdpiece_a.RDS
/usr/lib64/R/library/Rdpack/tests/testthat/char2Rdpiece_b.RDS
/usr/lib64/R/library/Rdpack/tests/testthat/char2Rdpiece_c.RDS
/usr/lib64/R/library/Rdpack/tests/testthat/classRepresentation-class.Rd
/usr/lib64/R/library/Rdpack/tests/testthat/get_sig_text_f1.RDS
/usr/lib64/R/library/Rdpack/tests/testthat/get_sig_text_f4.RDS
/usr/lib64/R/library/Rdpack/tests/testthat/initialize-methods.Rd
/usr/lib64/R/library/Rdpack/tests/testthat/myshow-methods.Rd
/usr/lib64/R/library/Rdpack/tests/testthat/show.Rd
/usr/lib64/R/library/Rdpack/tests/testthat/test-bib.R
/usr/lib64/R/library/Rdpack/tests/testthat/test-char2Rdpiece.R
/usr/lib64/R/library/Rdpack/tests/testthat/test-reprompt.R
