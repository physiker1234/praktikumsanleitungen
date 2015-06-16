%%
%% This is file `tudphygp_eng.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% tudphygp.dtx  (with options: `style')
%% 
%% Copyright (C) 2009 by AGeS -- www.ages-skripte.org
%% This file may be distributed and/or modified under the conditions of the LaTeX Project Public License, either version 1.2 of this license or (at your option) any later version. The latest version of this license is in:
%% 
%%   http://www.latex-project.org/lppl.txt
%% 
%% and version 1.2 or later is part of all distributions of LaTeX version 1999/12/01 or later.
\NeedsTeXFormat{LaTeX2e}[2005/12/01]
\ProvidesClass{tudphygp}
   [2009/04/06 1.0RC1 Klasse f�r die Anleitungen des physikalischen Grundpraktikums]
\DeclareOption{ltxdoc}{\def\tud@ltxdocIsLoaded{}}
\DeclareOption{platz}{\def\tud@buildAsPlatz{}}
\DeclareOption*{\PassOptionsToClass{scrartcl}}
\ProcessOptions\relax
\@ifundefined{tud@ltxdocIsLoaded}{%
 \LoadClass[11pt]{scrartcl}
 }{%
 \LoadClassWithOptions{ltxdoc}\endinput}
\RequirePackage{ifpdf}
\ifpdf\RequirePackage{cmap}\fi
\RequirePackage[english]{babel}
\RequirePackage[latin1]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{geometry}
\RequirePackage{calc}
\RequirePackage{tabularx}
\RequirePackage{graphicx}
\RequirePackage{amsmath,amssymb}
\RequirePackage{sistyle}
\RequirePackage{fancyhdr}
\RequirePackage{ifthen}
\RequirePackage[ngerman]{isodate}
\RequirePackage{picins}
\@ifundefined{tud@buildAsPlatz}{%
 \geometry{a4paper,twoside,inner=2cm,top=2.8cm,bottom=2.2cm}
}{%
 \geometry{a4paper,left=2cm,top=2.8cm,bottom=2.2cm}
}
\setlength{\parindent}{0pt}
\setlength{\parskip}{.5em}
\setcounter{secnumdepth}{3}
\SIstyle{German}
\fancypagestyle{plain}{\pagestyle{fancy}}
\pagestyle{fancy}
\fancyhf{}
\fancyhead{}
\fancyfoot{}
\renewcommand\headrulewidth{0pt}
\renewcommand\footrulewidth{0pt}
\newcommand\changefont[3]{%
 \fontfamily{#1}\fontseries{#2}\fontshape{#3} \selectfont}
\newcommand\versuch[3][Experiment:~]{\def\@versuchlabel{#1}\def\@versuch{#2}\def\@versuchkurz{#3}}
\versuch{Versuchsname}{??}
\title{\@versuch~(\@versuchkurz)}
\newcommand\bearbeitet[2]{\def\@bearbeitetPerson{#1}}%\def\@bearbeitetDatum{#2}}
\bearbeitet{}{}
\author{}
\date{}
\newlength\tud@SideHeaderLength
\newcommand\tud@Header[1]{%
 \fancyhead[C]{%
  \setlength\tud@SideHeaderLength{\widthof{\@versuchlabel\@versuchkurz}}
  \begin{tabularx}{\linewidth}{%
   @{}p{\tud@SideHeaderLength}@{}>{\centering}X@{}>{\hfill}p{\tud@SideHeaderLength}@{}}
  \@versuchlabel\@versuchkurz & #1 & Page~\thepage
  \end{tabularx}\vskip-1em%
}}%
\renewcommand\sectionmark[1]{%
 \renewcommand\headrulewidth{1pt}%
 \tud@Header{#1}%
}
\newcommand\tud@printList[1]{%
 \let\tud@plCurrentSep\tud@plInitSep
 \@for\tud@plItem:=#1\do{%
  \tud@plCurrentSep\tud@plItem%
 }%
}
\def\tud@plInitSep{\let\tud@plCurrentSep\tud@plSeparator}
\newcommand\tud@plSeparator{\newline}
\renewcommand\capfont{\normalfont\small}
\renewcommand\caplabelfont{\normalfont\small\bfseries}
\AtBeginDocument{
 \renewcommand\figurename{Abb.}
}
\@ifundefined{tud@buildAsPlatz}{
 \renewcommand\maketitle{%
  \numdate
  \begin{tabularx}{\linewidth}{@{}|p{\linewidth/2+.8cm}|X|@{}}
   \hline
   \parbox{\linewidth}{\vspace{1em}%
    \begin{minipage}{\linewidth}%
     \centering%
     \ifpdf\IfFileExists{TUD-Logo(sw).pdf}{%
       \includegraphics[width=\linewidth/2]{TUD-Logo(sw)}
      }{{\LARGE\bfseries Dresden University of Technology}}%
     \else\IfFileExists{TUD-Logo(sw).eps}{%
       \includegraphics[width=\linewidth/2]{TUD-Logo(sw)}
      }{{\LARGE\bfseries Dresden University of Technology}}%
     \fi\\[1em]
     {\large\bfseries Fachrichtung Physik}\\[.6em]
     Physikalisches Grundpraktikum
    \end{minipage}\vspace{1em}} &
   \parbox{\linewidth}{\vspace{1em}%
    \begin{minipage}{\linewidth}\centering%
     \resizebox{\linewidth/2}{!}{{\large \@versuchlabel}{%
      \Large\changefont{cmr}{bx}{n}\@versuchkurz}}\\[1em]
     \begin{tabularx}{\linewidth-.1cm}{l@{~}X}%\small\\%
     \ifthenelse{\equal{\@author}{}}{}{Created by: & \tud@printList{\@author}\\}%
     \ifthenelse{\equal{\@bearbeitetPerson}{}}{}{\footnotesize Edited: & \footnotesize\tud@printList{\@bearbeitetPerson}\\}%
     Updated: & on \today
     \end{tabularx}
   \end{minipage}\vspace{1em}}\\
   \hline
  \end{tabularx}\\[3em]
  \parbox{\linewidth}{%
   \flushleft\fontsize{17}{17}\changefont{cmss}{bx}{n}\@versuch}
  \vspace{3em}
  \tableofcontents
  \newpage
 }
}{%
 \renewcommand\maketitle{%
  \numdate
  \begin{tabularx}{\linewidth}{@{}|p{\linewidth/2+.8cm}|X|@{}}
   \hline
   \parbox{\linewidth}{\vspace{1em}%
    \begin{minipage}{\linewidth}%
     \hspace{2ex}
     \begin{minipage}[c]{4em}
      \ifpdf\IfFileExists{TUD-Icon(sw).pdf}{%
        \includegraphics[width=\linewidth]{TUD-Icon(sw)}
       }{{\LARGE\bfseries Dresden University of Technology}}%
      \else\IfFileExists{TUD-Icon(sw).eps}{%
        \includegraphics[width=\linewidth]{TUD-Icon(sw)}
       }{}%
      \fi
     \end{minipage}\hspace{2ex}
     \begin{minipage}[c]{\widthof{Physikalisches Grundpraktikum}}
      {\Large\bfseries TU~Dresden}\\
      {\large\bfseries Fachrichtung Physik}\\[1ex]
      Physikalisches Grundpraktikum
     \end{minipage}
    \end{minipage}\vspace{1em}} &
   \parbox{\linewidth}{\vspace{1em}%
    \begin{minipage}{\linewidth}\centering%
     \resizebox{4\linewidth/5}{!}{{\large Platzanleitung~}{%
      \Large\changefont{cmr}{bx}{n}\@versuchkurz}}\\[1em]
     \resizebox{4\linewidth/5}{!}{\@versuch}
   \end{minipage}\vspace{1em}}\\
   \hline
  \end{tabularx}
 }
}
\newcommand\optional[2]{
 \let\tud@thesection\thesection
 \let\tud@thesubsection\thesubsection
 \let\tud@thesubsubsection\thesubsubsection
 \def\thesection{\arabic{section}*}
 \def\thesubsection{\arabic{section}.\arabic{subsection}*}
 \def\thesubsubsection{\arabic{section}.\arabic{subsection}.\arabic{subsubsection}*}
 #1{#2}
 \let\thesection\tud@thesection
 \let\thesubsection\tud@thesubsection
 \let\thesubsubsection\tud@thesubsubsection
}
\def\tud@listOfQuestions{}
\def\tud@listOfLiterature{}
\newcommand\frageWithoutStar[1]{%
 \g@addto@macro{\tud@listOfQuestions}{\protect\item #1}
}
\newcommand\frageWithStar[1]{%
 \g@addto@macro{\tud@listOfQuestions}{\protect\stepcounter{enumi}\protect\item[\arabic{enumi}.${}^*$] #1}
 \global\def\tud@physikfrage{}
}
\def\frage{\@ifstar\frageWithStar\frageWithoutStar}
\newcounter{bookref}
\setcounter{bookref}{0}
\newcommand\buch[5]{%
 \expandafter\@ifundefined{book@#1}{%
  \expandafter\def\csname book@#1\endcsname{%
   #2,~\textit{#3},~#4,~#5%
  }
  \stepcounter{bookref}
  \global\expandafter\edef\csname bookref@#1\endcsname{\arabic{bookref}}
  \g@addto@macro\tud@listOfLiterature{%
   \protect\item[{[\csname bookref@#1\endcsname]}] \csname book@#1\endcsname}
  }{%
  \ClassError{tudphygp}{%
   Der Name `#1' ist bereits vergeben%
  }{Geben sie einen neuen Namen f�r `#1' an.}%
 }
}
\let\tud@enddocument\enddocument
\renewcommand\enddocument{%
 \ifthenelse{%
  \NOT\equal{\tud@listOfQuestions}{} \OR%
  \NOT\equal{\tud@listOfLiterature}{}}{%
   \vspace{1em}
   \begin{minipage}{\textwidth}
 }{}%
 \ifthenelse{\NOT\equal{\tud@listOfQuestions}{}}{%
  \section*{Questions}
  \addcontentsline{toc}{section}{Questions}
  \tud@Header{Questions}
   \begin{enumerate}\setlength\itemsep{-0.2em}
    \tud@listOfQuestions
   \end{enumerate}
 }{}%
 \ifthenelse{\NOT\equal{\tud@listOfLiterature}{}}{%
  \section*{Literature}
  \addcontentsline{toc}{section}{Literature}
  \tud@Header{Literature}
  \begin{itemize}\setlength\itemsep{-0.2em}
   \tud@listOfLiterature
  \end{itemize}
 }{}
 \ifthenelse{%
  \NOT\equal{\tud@listOfQuestions}{} \OR%
  \NOT\equal{\tud@listOfLiterature}{}}{%
   \end{minipage}
  \@ifundefined{tud@physikfrage}{}{
   \let\tud@savefootnote\thefootnote
   \renewcommand\thefootnote{${}^*$}
   \footnotetext{Nur f�r Physiker}
   \renewcommand\thefootnote\tud@savefootnote
  }
 }{}%
 \tud@enddocument%
}
\newcommand\verweis[2][]{%
 \@ifundefined{book@#2}{%
  \ClassWarningNoLine{tudphygp}{Das Buch `#2' wurde noch nicht definiert}
}{%
 \ifthenelse{\equal{#1}{}}{%
  [\csname bookref@#2\endcsname]%
 }{%
 [\csname bookref@#2\endcsname,~#1]%
}}}
\endinput
%%
%% End of file `tudphygp_eng.cls'.
