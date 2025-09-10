"use client";

import { Card } from "@/components/ui/Card";
import { BookOpen, FileText, Download } from "lucide-react";

export function ResourcesContent() {
  return (
    <div className="flex w-full h-full bg-[#22273433] backdrop-blur-sm relative p-6 overflow-y-auto">
      <div className="w-full">
        <h1 className="text-3xl font-bold text-white mb-8">Resources</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors">
            <div className="p-6">
              <div className="flex items-center gap-3 mb-4">
                <BookOpen className="w-8 h-8 text-indigo-400" />
                <h3 className="text-xl font-semibold text-white">Wellness Guide</h3>
              </div>
              <p className="text-gray-400 mb-4">Complete mental health handbook</p>
              <button className="flex items-center gap-2 text-blue-400 hover:text-blue-300 transition-colors">
                <Download className="w-4 h-4" />
                <span className="text-sm">Download PDF</span>
              </button>
            </div>
          </Card>
          <Card className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors">
            <div className="p-6">
              <div className="flex items-center gap-3 mb-4">
                <FileText className="w-8 h-8 text-green-400" />
                <h3 className="text-xl font-semibold text-white">Articles</h3>
              </div>
              <p className="text-gray-400 mb-4">Latest research and insights</p>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
