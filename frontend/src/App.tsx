import "./App.css";

import Header from "./components/layout/Header";
import InteractionForm from "./components/interaction/InteractionForm";
import ChatPanel from "./components/chat/ChatPanel";

function App() {
  return (
    <div className="app">
      <Header />

      <main className="main-layout">
        <section className="left-panel">
          <InteractionForm />
        </section>

        <section className="right-panel">
          <ChatPanel />
        </section>
      </main>
    </div>
  );
}

export default App;
