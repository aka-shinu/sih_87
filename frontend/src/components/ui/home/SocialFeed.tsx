"use client";

import { Heart, MessageCircle, Share, MoreHorizontal, Clock } from "lucide-react";
import { SocialFeedProps } from "@/types/home";

export function SocialFeed({ socialFeed }: SocialFeedProps) {
  return (
    <div className="mb-8 pl-4">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold text-white">Community Feed</h2>
        <button className="text-blue-400 hover:text-blue-300 text-sm font-medium transition-colors">
          View all
        </button>
      </div>
      <div className="space-y-3">
        {socialFeed.map((post) => (
          <div key={post.id} className="bg-gray-800/30 rounded-2xl overflow-hidden hover:bg-gray-800/50 transition-all duration-300 hover:shadow-lg hover:scale-[1.01] group">
            <div className="p-5">
              <div className="flex items-start gap-4 mb-4">
                <div className="relative">
                  <div className="w-12 h-12 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center ring-2 ring-gray-700 group-hover:ring-blue-500 transition-all duration-300">
                    <span className="text-white font-bold text-lg">
                      {post.user.username.charAt(1).toUpperCase()}
                    </span>npm
                  </div>
                  <div className="absolute -bottom-1 -right-1 w-4 h-4 bg-green-500 rounded-full border-2 border-gray-800"></div>
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center gap-2">
                      <h4 className="font-bold text-white text-base group-hover:text-blue-300 transition-colors">{post.user.name}</h4>
                      <span className="text-[50%] text-gray-500">•</span>
                      <span className="text-gray-400 text-sm font-mono">{post.user.username}</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <div className="flex items-center gap-1 text-gray-500 text-sm">
                        <Clock className="w-3 h-3" />
                        {post.time}
                      </div>
                      <button className="text-gray-500 hover:text-gray-300 transition-colors">
                        <MoreHorizontal className="w-4 h-4" />
                      </button>
                    </div>
                  </div>
                  <p className="text-gray-200 text-sm leading-relaxed mb-3">{post.content}</p>
                  
                  {post.image && (
                    <div className="mb-3 rounded-2xl overflow-hidden group/image">
                      <img 
                        src={post.image} 
                        alt="Post content"
                        className="w-full h-48 object-cover group-hover/image:scale-105 transition-transform duration-500 ease-out"
                      />
                    </div>
                  )}
                </div>
              </div>
              
              <div className="flex items-center justify-between pt-3 border-t border-gray-700/30">
                <div className="flex items-center gap-5">
                  <button className="flex items-center gap-2 text-gray-400 hover:text-red-400 transition-all duration-200 group">
                    <Heart className="w-4 h-4 group-hover:scale-110 transition-transform" />
                    <span className="text-sm font-medium">{post.likes}</span>
                  </button>
                  <button className="flex items-center gap-2 text-gray-400 hover:text-blue-400 transition-all duration-200 group">
                    <MessageCircle className="w-4 h-4 group-hover:scale-110 transition-transform" />
                    <span className="text-sm font-medium">{post.comments}</span>
                  </button>
                  <button className="flex items-center gap-2 text-gray-400 hover:text-green-400 transition-all duration-200 group">
                    <Share className="w-4 h-4 group-hover:scale-110 transition-transform" />
                    <span className="text-sm font-medium">Share</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
