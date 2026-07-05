import { useState } from "react";
import "./index.css";

type Regulation = "GDPR" | "KVKK";
type ViewState = "upload" | "loading" | "result";

const mockResult = {
  regulation: "gdpr",
  document_name: "privacy-policy.pdf",
  overall_score: 62,
  results: [
    {
      article_id: "gdpr-art-13",
      title: "Bilgilendirme Yükümlülüğü",
      status: "partial",
      evidence: "We collect your name, email, and usage data...",
      evidence_location: "sayfa 1, paragraf 2",
      recommendation: "Hukuki dayanak ve saklama süresi eklenmeli.",
    },
    {
      article_id: "gdpr-art-6",
      title: "Hukuki Dayanak",
      status: "missing",
      evidence: null,
      evidence_location: null,
      recommendation:
        "Verinin hangi hukuki gerekçeyle işlendiği belirtilmeli.",
    },
    {
      article_id: "gdpr-art-32",
      title: "İşleme Güvenliği",
      status: "met",
      evidence:
        "The document references encryption, access control and internal security procedures.",
      evidence_location: "sayfa 2, paragraf 1",
      recommendation: "Mevcut güvenlik önlemleri korunmalı ve düzenli test edilmeli.",
    },
  ],
};


export default function App() {
  const [fileName, setFileName] = useState("");
  const [regulation, setRegulation] = useState<Regulation>("GDPR");
  const [view, setView] = useState<ViewState>("upload");
  const [error, setError] = useState("");

  function handleFileChange(event: React.ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0];
    setError("");

    if (!file) return;

    const allowedTypes = [".pdf", ".doc", ".docx", ".txt"];
    const isAllowed = allowedTypes.some((type) =>
      file.name.toLowerCase().endsWith(type)
    );

    if (!isAllowed) {
      setFileName("");
      setError("Unsupported file type. Please upload PDF, DOCX or TXT.");
      return;
    }

    if (file.size > 10 * 1024 * 1024) {
      setFileName("");
      setError("File size is too large. Maximum allowed size is 10MB.");
      return;
    }

    setFileName(file.name);
  }

  function handleAnalyze() {
    if (!fileName) {
      setError("Please upload a document before starting the analysis.");
      return;
    }

    setError("");
    setView("loading");

    setTimeout(() => {
      setView("result");
    }, 2200);
  }

  function resetFlow() {
    setFileName("");
    setError("");
    setView("upload");
  }

  return (
    <main className="min-h-screen bg-[#f7f8f4] text-slate-950">
      <nav className="sticky top-0 z-50 border-b border-slate-200/70 bg-[#f7f8f4]/90 backdrop-blur-xl">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-5">
          <div className="text-3xl font-black tracking-tight text-emerald-950">
            Traceon
          </div>

          <div className="hidden items-center gap-8 text-sm font-semibold text-slate-700 md:flex">
            <a href="#product">Product</a>
            <a href="#how">How it works</a>
            <a href="#features">Features</a>
            <a href="#upload">Upload</a>
          </div>

          <div className="flex items-center gap-3">
            <button className="hidden rounded-full border border-slate-300 px-5 py-2.5 text-sm font-bold md:block">
              Log in
            </button>
            <button className="rounded-full bg-emerald-600 px-5 py-2.5 text-sm font-black text-white shadow-lg shadow-emerald-600/20 hover:bg-emerald-500">
              Get started →
            </button>
          </div>
        </div>
      </nav>

      <section id="product" className="relative overflow-hidden border-b border-slate-200">
        <div className="absolute left-1/2 top-10 h-[520px] w-[520px] -translate-x-1/2 rounded-full bg-emerald-300/30 blur-[120px]" />

        <div className="relative mx-auto grid max-w-7xl gap-12 px-8 py-10 lg:grid-cols-[1fr_0.95fr] lg:items-center">
          <div>
            <div className="mb-6 inline-flex rounded-full border border-emerald-200 bg-white px-4 py-2 text-sm font-black text-emerald-700 shadow-sm">
              AI Compliance Copilot for GDPR & KVKK
            </div>

            <h1 className="max-w-3xl text-5xl font-black leading-[0.95] tracking-tight text-slate-950 md:text-7xl">
              Compliance, understood in minutes.
            </h1>

            <p className="mt-6 max-w-xl text-lg leading-8 text-slate-600">
              Upload your compliance documents and receive an AI-powered
              pre-assessment with risk signals, article mapping and supporting
              evidence.
            </p>

            <div className="mt-8 flex flex-wrap gap-4">
              <a
                href="#upload"
                className="rounded-full bg-emerald-600 px-6 py-3 font-black text-white shadow-xl shadow-emerald-600/20 hover:bg-emerald-500"
              >
                Analyze document →
              </a>
              <button className="rounded-full border border-slate-300 bg-white px-6 py-3 font-black text-slate-800 hover:border-emerald-300">
                View sample report
              </button>
            </div>

            <div className="mt-8 grid max-w-2xl gap-3 sm:grid-cols-2">
              {[
                "Evidence-based findings",
                "Risk scoring",
                "GDPR & KVKK support",
                "API-ready workflow",
              ].map((item) => (
                <div
                  key={item}
                  className="rounded-2xl border border-slate-200 bg-white px-5 py-4 text-sm font-bold text-slate-700 shadow-sm"
                >
                  <span className="mr-2 text-emerald-600">✓</span>
                  {item}
                </div>
              ))}
            </div>
          </div>

          <section
            id="upload"
            className="rounded-[2rem] border border-slate-200 bg-white p-5 shadow-2xl shadow-emerald-900/10"
          >
            {view === "upload" && (
              <>
                <div className="mb-6">
                  <p className="text-sm font-black text-emerald-600">
                    Document Analysis
                  </p>
                  <h2 className="mt-2 text-3xl font-black">Upload document</h2>
                  <p className="mt-3 text-sm leading-6 text-slate-500">
                    Select a regulation, upload your file and start the compliance
                    pre-assessment.
                  </p>
                </div>

                <div className="mb-5">
                  <label className="mb-3 block text-sm font-black text-slate-700">
                    Regulation framework
                  </label>

                  <div className="grid grid-cols-2 gap-3">
                    {(["GDPR", "KVKK"] as Regulation[]).map((item) => (
                      <button
                        key={item}
                        onClick={() => setRegulation(item)}
                        className={`rounded-2xl border px-4 py-3 text-sm font-black transition ${regulation === item
                          ? "border-emerald-500 bg-emerald-50 text-emerald-700"
                          : "border-slate-200 bg-slate-50 text-slate-500 hover:border-emerald-300"
                          }`}
                      >
                        {item}
                      </button>
                    ))}
                  </div>
                </div>

                <label
                  htmlFor="file"
                  className="group flex cursor-pointer flex-col items-center justify-center rounded-[1.75rem] border-2 border-dashed border-emerald-200 bg-emerald-50/50 px-6 py-8 text-center transition hover:border-emerald-500 hover:bg-emerald-50"
                >
                  <div className="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-white text-emerald-600 shadow-sm transition group-hover:scale-105">
                    ↑
                  </div>

                  <p className="text-xl font-black">Drop your file here</p>
                  <p className="mt-2 text-sm text-slate-500">
                    or click to browse from your computer
                  </p>

                  <div className="mt-4 flex gap-2 text-xs font-bold text-slate-500">
                    <span className="rounded-full border border-slate-200 bg-white px-3 py-1">PDF</span>
                    <span className="rounded-full border border-slate-200 bg-white px-3 py-1">DOCX</span>
                    <span className="rounded-full border border-slate-200 bg-white px-3 py-1">TXT</span>
                  </div>

                  {fileName && (
                    <div className="mt-5 max-w-full rounded-full border border-emerald-200 bg-white px-4 py-2 text-sm font-black text-emerald-700">
                      {fileName}
                    </div>
                  )}

                  <input
                    id="file"
                    type="file"
                    accept=".pdf,.doc,.docx,.txt"
                    onChange={handleFileChange}
                    className="hidden"
                  />
                </label>

                {error && (
                  <div className="mt-4 rounded-2xl border border-red-200 bg-red-50 px-4 py-3 text-sm font-bold text-red-700">
                    {error}
                  </div>
                )}

                <button
                  onClick={handleAnalyze}
                  disabled={!fileName}
                  className="mt-5 w-full rounded-2xl bg-emerald-600 px-5 py-3 font-black text-white transition hover:bg-emerald-500 disabled:cursor-not-allowed disabled:bg-slate-200 disabled:text-slate-400"
                >
                  Analyze Compliance →
                </button>
              </>
            )}

            {view === "loading" && (
              <div className="flex min-h-[520px] flex-col items-center justify-center text-center">
                <div className="mb-6 h-16 w-16 animate-spin rounded-full border-4 border-emerald-100 border-t-emerald-600" />
                <p className="text-sm font-black text-emerald-600">
                  Analyzing document
                </p>
                <h2 className="mt-3 text-3xl font-black">
                  Building compliance report...
                </h2>
                <p className="mt-3 max-w-md text-sm leading-6 text-slate-500">
                  Traceon is checking the selected document against {regulation}
                  controls and extracting evidence.
                </p>

                <div className="mt-8 w-full max-w-md space-y-3 text-left">
                  {[
                    "Reading document content",
                    "Mapping clauses to regulation articles",
                    "Extracting evidence snippets",
                    "Preparing risk overview",
                  ].map((step) => (
                    <div
                      key={step}
                      className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm font-bold text-slate-700"
                    >
                      <span className="mr-2 text-emerald-600">✓</span>
                      {step}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {view === "result" && (
              <div>
                <div className="mb-4 flex items-start justify-between gap-4">
                  <div>
                    <p className="text-xs font-black uppercase tracking-wide text-emerald-600">
                      Compliance Report
                    </p>
                    <h2 className="mt-1 text-2xl font-black">Analysis result</h2>
                    <p className="mt-1 text-xs text-slate-500">
                      Mock result generated for {fileName}
                    </p>
                  </div>

                  <div className="rounded-2xl bg-emerald-50 px-4 py-3 text-center">
                    <p className="text-2xl font-black text-emerald-700">
                      {mockResult.overall_score}
                    </p>
                    <p className="text-xs font-black text-emerald-700">Score</p>
                  </div>
                </div>

                <div className="mb-3 rounded-2xl border border-amber-200 bg-amber-50 px-4 py-2 text-sm font-black text-amber-700">
                  Overall score: {mockResult.overall_score}/100
                </div>

                <div className="space-y-3">
                  {mockResult.results.map((finding) => (
                    <div
                      key={finding.article_id}
                      className="rounded-2xl border border-slate-200 bg-slate-50 p-3"
                    >
                      <div className="mb-1 flex items-center justify-between gap-3">
                        <p className="text-xs font-black text-slate-900">
                          {finding.article_id}
                        </p>

                        <span
                          className={`rounded-full px-3 py-1 text-xs font-black ${finding.status === "met"
                              ? "bg-emerald-100 text-emerald-700"
                              : finding.status === "partial"
                                ? "bg-amber-100 text-amber-700"
                                : "bg-red-100 text-red-700"
                            }`}
                        >
                          {finding.status}
                        </span>
                      </div>

                      <h3 className="text-base font-black">{finding.title}</h3>

                      {finding.evidence && (
                        <p className="mt-1 text-sm leading-5 text-slate-600">
                          {finding.evidence}
                        </p>
                      )}

                      {finding.evidence_location && (
                        <p className="mt-1 text-xs font-bold text-slate-500">
                          Evidence location: {finding.evidence_location}
                        </p>
                      )}

                      <p className="mt-2 text-sm font-bold text-emerald-700">
                        Recommendation: {finding.recommendation}
                      </p>
                    </div>
                  ))}
                </div>

                <button
                  onClick={resetFlow}
                  className="mt-4 w-full rounded-2xl border border-slate-300 bg-white px-5 py-2.5 font-black text-slate-800 hover:border-emerald-400"
                >
                  Analyze another document
                </button>
              </div>
            )}          </section>
        </div>
      </section>
    </main>
  );
}